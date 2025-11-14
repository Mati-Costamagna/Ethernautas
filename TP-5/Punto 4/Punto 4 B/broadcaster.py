import paho.mqtt.client as mqtt
import time
import config

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Cliente Central conectado exitosamente")
    else:
        print(f"Error de conexión. Código: {rc}")

def on_publish(client, userdata, mid, properties=None):
    print(f"Mensaje broadcast enviado (ID: {mid})")

# Crear cliente con CallbackAPIVersion
client = mqtt.Client(
    client_id="ClienteCentral",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_publish = on_publish

print("Conectando Cliente Central...")
client.connect(config.BROKER, config.PORT, 60)
client.loop_start()

# Enviar mensajes broadcast
try:
    contador = 0
    print("\n Enviando broadcasts a toda la LAN...")
    print("Presiona Ctrl+C para detener\n")
    
    while True:
        mensaje = f"Broadcast #{contador}: Anuncio general a toda la LAN"
        client.publish("lan/broadcast/all", mensaje, qos=1)
        print(f"Enviando: {mensaje}")
        contador += 1
        time.sleep(8)
        
except KeyboardInterrupt:
    print("\n\nDeteniendo Cliente Central...")
    client.loop_stop()
    client.disconnect()
    print("Cliente Central desconectado")