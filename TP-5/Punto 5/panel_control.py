import paho.mqtt.client as mqtt
import config
import time

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Panel de Control conectado\n")
    else:
        print(f"Error: {rc}")

# Crear cliente
client = mqtt.Client(
    client_id="PanelControl",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set()
client.on_connect = on_connect

print("Conectando Panel de Control...")
client.connect(config.BROKER, config.PORT, 60)
client.loop_start()

time.sleep(2)

print("="*50)
print("PANEL DE CONTROL - SENSORES")
print("="*50)
print("\nComandos:")
print("  1 - START (Iniciar sensores)")
print("  2 - STOP  (Detener sensores)")
print("  3 - Salir")
print("="*50)

try:
    while True:
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            client.publish("lan/broadcast/command", "START", qos=1)
            print("Comando START enviado")
        elif opcion == "2":
            client.publish("lan/broadcast/command", "STOP", qos=1)
            print("Comando STOP enviado")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
            
except KeyboardInterrupt:
    print("\nCerrando...")
finally:
    client.loop_stop()
    client.disconnect()