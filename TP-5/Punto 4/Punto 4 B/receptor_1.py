import paho.mqtt.client as mqtt
import config

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Receptor 1 conectado exitosamente")
        # Suscribirse usando wildcard # para recibir todos los broadcasts
        client.subscribe("lan/broadcast/#", qos=1)
        print("Suscrito a: lan/broadcast/#")
    else:
        print(f"Error de conexión: {rc}")

def on_message(client, userdata, msg):
    print(f"\n{'='*60}")
    print(f"[RECEPTOR 1 - BROADCAST RECIBIDO]")
    print(f"{'='*60}")
    print(f"Tópico: {msg.topic}")
    print(f"Mensaje: {msg.payload.decode()}")
    print(f"QoS: {msg.qos}")
    print(f"{'='*60}\n")

# Crear cliente con CallbackAPIVersion
client = mqtt.Client(
    client_id="Receptor1",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

print("="*60)
print("RECEPTOR 1 - Esperando broadcasts...")
print("="*60)
client.connect(config.BROKER, config.PORT, 60)

try:
    print("\nEsperando mensajes... (Ctrl+C para salir)\n")
    client.loop_forever()
except KeyboardInterrupt:
    print("\n\nCerrando Receptor 1...")
    client.disconnect()
    print("Receptor 1 desconectado")