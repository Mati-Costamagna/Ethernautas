import paho.mqtt.client as mqtt
import csv
import json
from datetime import datetime
import config

# Archivo para guardar datos
CSV_FILE = "datos_sensores.csv"
JSON_FILE = "datos_sensores.json"

datos_recolectados = []

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Gateway conectado")
        # Suscribirse a todos los sensores
        client.subscribe("lan/+/sensor/#", qos=1)
        print("Suscrito a: lan/+/sensor/#")
        print("Esperando datos...\n")
    else:
        print(f"Error de conexión: {rc}")

def on_message(client, userdata, msg):
    # Extraer información del tópico
    # Ejemplo: lan/sala1/sensor/temp
    partes = msg.topic.split('/')
    sala = partes[1]
    tipo_sensor = partes[3]
    valor = msg.payload.decode()
    
    # Crear registro
    registro = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'sala': sala,
        'tipo_sensor': tipo_sensor,
        'valor': float(valor),
        'topico': msg.topic
    }
    
    datos_recolectados.append(registro)
    
    # Mostrar en consola
    print(f"[DATO RECOLECTADO #{len(datos_recolectados)}]")
    print(f"Timestamp: {registro['timestamp']}")
    print(f"Sala: {registro['sala']}")
    print(f"Sensor: {registro['tipo_sensor']}")
    print(f"Valor: {registro['valor']}")
    print("-" * 50)
    
    # Guardar en CSV
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'sala', 'tipo_sensor', 'valor', 'topico'])
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(registro)
    
    # Guardar en JSON
    with open(JSON_FILE, 'w') as f:
        json.dump(datos_recolectados, f, indent=2)

# Crear cliente
client = mqtt.Client(
    client_id="Gateway",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.username_pw_set(config.USERNAME, config.PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

print("Iniciando Gateway...")
client.connect(config.BROKER, config.PORT, 60)

try:
    print("Recolectando datos... (Ctrl+C para salir)\n")
    client.loop_forever()
except KeyboardInterrupt:
    print(f"\n\nCerrando Gateway...")
    print(f"Total datos recolectados: {len(datos_recolectados)}")
    print(f"Datos guardados en: {CSV_FILE} y {JSON_FILE}")
    client.disconnect()