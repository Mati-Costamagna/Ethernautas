import pandas as pd
import matplotlib.pyplot as plt

# Datos de los protocolos: {protocolo: [alcance_min, alcance_max, data_rate_min, data_rate_max]}
datos = {
    'Wi-Fi': [20, 100, 1e6, 1e9],
    'Bluetooth': [1, 100, 1e3, 1e6],
    'ZigBee': [10, 100, 20e3, 250e3],
    'NFC': [0.01, 0.20, 106e3, 424e3],
    'LTE': [100, 10000, 1e6, 1e9],
    'GSM': [100, 35000, 9.6e3, 40e3],
    '5G': [100, 1000, 1e9, 10e9],
    'LoRa': [1000, 15000, 300, 50e3],
    'NB-IoT': [1000, 10000, 20e3, 250e3],
    'SigFox': [5000, 50000, 100, 600],
    'Z-Wave': [30, 100, 9.6e3, 100e3],
}

# Crear listas para los puntos del gráfico
nombres_protocolos = []
distancias_promedio = []
data_rates_promedio = []

for protocolo, valores in datos.items():
    nombres_protocolos.append(protocolo)
    # Calcular el valor promedio para el gráfico
    distancia_promedio = (valores[0] + valores[1]) / 2
    data_rate_promedio = (valores[2] + valores[3]) / 2
    
    distancias_promedio.append(distancia_promedio)
    data_rates_promedio.append(data_rate_promedio)

# Crear el DataFrame de pandas para mostrar los datos en forma de tabla
df = pd.DataFrame({
    'Protocolo': nombres_protocolos,
    'Distancia (m)': distancias_promedio,
    'Data Rate (bps)': data_rates_promedio
})

plt.figure(figsize=(12, 8))
plt.scatter(df['Distancia (m)'], df['Data Rate (bps)'], s=150, alpha=0.8, color='b')

for i, txt in enumerate(nombres_protocolos):
    plt.annotate(txt, (df['Distancia (m)'][i], df['Data Rate (bps)'][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.xscale('log')
plt.yscale('log')

plt.title('Alcance vs. Tasa de Datos de Protocolos Inalámbricos')
plt.xlabel('Distancia (m) [Escala logarítmica]')
plt.ylabel('Tasa de Datos (bps) [Escala logarítmica]')
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.xticks([1, 10, 100, 1000, 10000], ['1m', '10m', '100m', '1km', '10km'])
plt.yticks([1, 1e3, 1e6, 1e9], ['1', '1K', '1M', '1G'])

plt.tight_layout()
plt.show()