import paho.mqtt.client as mqtt
import time
import random
import config

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Sensor Temperatura Sala 1 conectado")
        # Suscribirse a comandos
        client.subscribe("lan/broadcast/command", qos=1)
        print("Esperando comando START...")
    else:
        print(f"Error de conexión: {rc}")

def on_message(client, userdata, msg):
    comando = msg.payload.decode()
    print(f"\nComando recibido: {comando}")
    
    if comando == "START":
        userdata['activo'] = True
        print("Sensor activado")
    elif comando == "STOP":
        userdata['activo'] = False
        print("Sensor detenido")

# Crear cliente
user_data = {'activo': False}
client = mqtt.Client(
    client_id="SensorTempSala1",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1,
    userdata=user_data
)
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

print("Conectando Sensor Temperatura Sala 1...")
client.connect(config.BROKER, config.PORT, 60)
client.loop_start()

try:
    while True:
        if user_data['activo']:
            # Generar temperatura aleatoria entre 18 y 28 grados
            temperatura = round(random.uniform(18.0, 28.0), 2)
            client.publish("lan/sala1/sensor/temp", str(temperatura), qos=1)
            print(f"Temperatura: {temperatura}°C")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nDeteniendo sensor...")
    client.loop_stop()
    client.disconnect()