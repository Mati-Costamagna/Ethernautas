import paho.mqtt.client as mqtt
import time
import config

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Dispositivo A conectado exitosamente al broker")
    else:
        print(f"Error de conexión. Código: {rc}")

def on_publish(client, userdata, mid, properties=None):
    print(f"Mensaje publicado con ID: {mid}")

# Crear cliente con CallbackAPIVersion
client = mqtt.Client(
    client_id="DispositivoA",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set()  # Habilitar TLS

# Callbacks
client.on_connect = on_connect
client.on_publish = on_publish

# Conectar
print("Conectando Dispositivo A al broker...")
client.connect(config.BROKER, config.PORT, 60)
client.loop_start()

# Publicar mensajes periódicamente
try:
    contador = 0
    while True:
        mensaje = f"Estado del Dispositivo A - Mensaje #{contador}"
        result = client.publish("lan/deviceA/status", mensaje, qos=1)
        print(f"Publicando: {mensaje}")
        contador += 1
        time.sleep(5)
except KeyboardInterrupt:
    print("\nDeteniendo Dispositivo A...")
    client.loop_stop()
    client.disconnect()