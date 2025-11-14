# dispositivo_b.py
import paho.mqtt.client as mqtt
import config

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Dispositivo B conectado exitosamente al broker")
        # Suscribirse al tópico
        client.subscribe("lan/deviceA/status", qos=1)
        print("Suscrito a: lan/deviceA/status")
    else:
        print(f"Error de conexión. Codigo: {rc}")

def on_message(client, userdata, msg):
    print(f"\n[MENSAJE RECIBIDO]")
    print(f"Tópico: {msg.topic}")
    print(f"Payload: {msg.payload.decode()}")
    print(f"QoS: {msg.qos}")
    print("-" * 50)

# Crear cliente con CallbackAPIVersion
client = mqtt.Client(
    client_id="DispositivoB",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set()

# Callbacks
client.on_connect = on_connect
client.on_message = on_message

# Conectar y mantener escuchando
print("Conectando Dispositivo B al broker...")
client.connect(config.BROKER, config.PORT, 60)

try:
    print("Esperando mensajes... (Ctrl+C para salir)")
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDeteniendo Dispositivo B...")
    client.disconnect()