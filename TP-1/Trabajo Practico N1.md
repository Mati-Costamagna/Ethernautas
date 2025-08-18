# Trabajo Práctico 1

**Nombres**  

_María Pilar Sabena_

_Mateo Quispe_

_Nicolas De la Mata_  

_Matias J. Costamagna_

**Grupo:** _Ethernautas_ 

**Facultad de Ciencias Exactas, Físicas y Naturales**  

**Asignatura:** _Comunicaciones de Datos_

**Profesores**
_Miguel Á. Solinas_
_Santiago M. Henn_
_Facundo Oliva Cuneo_

**Fecha:** _Agosto, 2025_

---

### Introducción

En este trabajo práctico se revisan conceptos básicos de ondas electromagnéticas, transmisión de datos y técnicas de modulación, para luego aplicarlos en una simulación con Packet Tracer. El objetivo es relacionar la teoría con un caso práctico de conectividad en una red simple, comprobando fenómenos como la atenuación de la señal y la verificación de conectividad entre dispositivos.

---

### Desarrollo

- 1

    - b 

    Para obtener el valor de la frecuencia, utilizamos la fórmula que relaciona la velocidad a la que viaja una onda con la longitud de dicha onda.
    La longitud de onda $\lambda$ es la distancia que recorre la onda hasta completar un ciclo, lo que en la imagen se indica como 60 [mm] (o $60e^{-3}$ [m]).

    $f [Hz] = \frac{c}{\lambda} = \frac{3e^8 [m/s]}{60e^{-3} [m]} = 5e^9 [Hz] = 5 [GHz]$

    - c

    La onda del punto _a_, tiene una frecuencia de 5 [GHz], por lo que la banda correspondiente que incluye esta frecuencia es la banda Banda de Frecuencia Super Alta (Super High Frequency o SHF), que abarca frecuencias entre 3 [GHz] y 30 [GHz] [1].

    - d

    Dispositivos que usan ondas en esta banda de frecuencias, son los aquellos que trabajan con redes WLAN, distintas comunicaciones satelitales, Internet, etc., como por ejemplo, los routers inalámbricos.

    - e

    La línea de trazos representa la disminución de la intensidad de la onda conforme se propaga en el medio. Esto tiene sentido ya que la intensidad es una propiedad de la onda que representa la cantidad de energía que esta transporta por unidad de tiempo y área, según la siguiente relación: $I [W/m^2]= \frac{Energía \cdot Tiempo}{Área} = \frac {Potencia}{Área}$. Por lo tanto, a medida que aumenta la distancia que recorrió la onda, la intensidad cae.

    - f

    En el ejemplo del router inalámbrico, el fenómeno se puede apreciar claramente, ya que la intensidad de la señal se ve afectada cuando hay una mayor distancia y/o la señal debe atravesar paredes para llegar desde el router inalámbrico hasta el dispositivo final.

    - g 

        - i

        Este fenómeno, solo afecta a la transmisión de telefonía celular, ya que esta se realiza por medio de ondas electromagnéticas. Se puede ver reflejado cuando una persona se encuentra en areás rurales, o edificios y sótanos, en donde la señal se atenúa debido a las largas distancias y gran cantidad de obstáculos que debe atravesar.
        - ii

        Por otro lado, las transmisiones por cable coaxial se realizan por medio de impulsos eléctricos por que lo que la pérdida de intensidad se da a causa de otros fenómenos.
        - iii

        En el caso la fibra óptica, la transmisión se basa en el envío y deteccón de impulsos de luz y al ser la luz una onda electromagnética, también se ve afectada por el fenómeno de pérdida de intensidad.

- 2

    - a 

    La representación muestra un esquema de una transmisión seria síncrona.

    - b

    No, el paradigma que permite transmitir datos a mayor velocidad es la transmisión paralela.

    - c

    La letra a transimitir sería la _e_ y su señal tendría la forma del siguiente diagrama:
    [\[Diagrama\]](https://drive.google.com/file/d/1ShVEO-wTh1o_AbqBXo0NTqEY3Yr3nFe3/view?usp=drive_link)

    - d

    Mediriamos la señal en los instantes temporales correspondientes a flancos descendentes del clock, ya que allí la señal permanece constante.

- 3

    - a

    El gráfico corresponde a una modulación PSK, que consiste principalmente en transmitir datos cambiando la fase de la onda portadora.

    - b

    [\[Modulación de Señal Digital\]](https://drive.google.com/file/d/18Vvu5ebEGoiLe8aUYSh7AZtYAY6-sgY8/view?usp=drive_link)

    - c

    Si hablamos de modulaciones de señales analógicas para datos digitales, otras técnicas similares, son la FSK, ASK, QAM y todas sus variantes dependiendo de la cantidad de símbolos distintos que se quieran transmitir [2].

    - d

    El BER es un parámetro que indica que tan bueno es el desempeño de un sistema de comunicación determinado.
    Fundamentalmente indica la probabilidad de error por bit transmitido.
    La técnica de modulación con mejores prestaciones es la PSK, la comparación entre las técnicas y sus eficiencias se encuentra desarrollada en el libro [2].

- 4

    - a

    La frecuencia a la que opera el router es 2.4 [GHz], la cual está incluida en la banda de Frecuencias Ultra Altas (Ultra High Frequency o UHF) que abarca desde los 300 [MHz] hasta los 3 [GHz]

    - g

    Para comprobar la conectividad entre las computadoras se utilizaran los comandos _ping_ y _tracert_. 
    
    El _ping_ envía paquetes al destino y espera la respuesta de este último. Sirve para comprobar si un dispositivo responde y está accesible en la red.

    El _tracrt_ envía paquetes al destino con un TTL (Time To Live) que va aumentando en cada intento. Cada dispositivo por el que pasa el paquete reduce ese TTL y responde cuando llega a 0. Esto permite descubrir la ruta (los saltos intermedios) que siguen los paquetes hasta llegar al destino.
    
    **Pruebas**

    IP PC: 192.168.0.102
    IP Notebook: 192.168.0.101
    Gateway: 192.168.0.1

    _Prueba 1_

    Desde la Notebook se utiliza ping a la IP de la PC: ping 192.168.0.102
    
    Respuesta: 
    Pinging 192.168.0.102 with 32 bytes of data:

    Reply from 192.168.0.102: bytes=32 time=20ms TTL=128
    Reply from 192.168.0.102: bytes=32 time=10ms TTL=128
    Reply from 192.168.0.102: bytes=32 time=12ms TTL=128
    Reply from 192.168.0.102: bytes=32 time=13ms TTL=128

    Ping statistics for 192.168.0.102:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 10ms, Maximum = 20ms, Average = 13ms

    _Prueba 2_

    Desde la PC se utiliza ping a la IP de la Notebook: ping 192.168.0.101
    
    Respuesta: 
    Pinging 192.168.0.101 with 32 bytes of data:

    Reply from 192.168.0.101: bytes=32 time=13ms TTL=128
    Reply from 192.168.0.101: bytes=32 time=13ms TTL=128
    Reply from 192.168.0.101: bytes=32 time=9ms TTL=128
    Reply from 192.168.0.101: bytes=32 time=7ms TTL=128

    Ping statistics for 192.168.0.101:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 7ms, Maximum = 13ms, Average = 10ms

    _Prueba 3_

    Trace Route desde la PC a la Notebook: tracert 192.168.0.101
    
    Respuesta:
    Tracing route to 192.168.0.101 over a maximum of 30 hops: 

        1   17 ms     10 ms     9 ms      192.168.0.101

    Trace complete

    La razón por la cual no aparece el router en la ruta de destino, es porque ambas computadoras estan dentro de una red   LAN, por lo que no es necesario pasar por el router para llegar al otro equipo.

    - h
    IP Notebook externa: 192.168.0.103
    Gateway: 192.168.0.1

    _Prueba: Notebook externa dentro del rango de la señal_

    Desde la Notebook externa se utiliza ping a la IP de la PC dentro de la oficina: ping 192.168.0.102
    
    Respuesta:     
    Pinging 192.168.0.102 with 32 bytes of data:

    Reply from 192.168.0.102: bytes=32 time=53ms TTL=128
    Reply from 192.168.0.102: bytes=32 time=14ms TTL=128
    Reply from 192.168.0.102: bytes=32 time=22ms TTL=128
    Reply from 192.168.0.102: bytes=32 time=11ms TTL=128

    Ping statistics for 192.168.0.102:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 11ms, Maximum = 53ms, Average = 25ms

    _Prueba: Notebook externa feura del rango de la señal_

    Desde la Notebook externa se utiliza ping a la IP de la PC dentro de la oficina: ping 192.168.0.102

    Respuesta
    Pinging 192.168.0.102 with 32 bytes of data:

    Request timed out.
    Request timed out.
    Request timed out.
    Request timed out.

    Ping statistics for 192.168.0.102:
        Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)


    **Conclusiones**

    Comparando los tiempos de viaje de los paquetes para el caso de la notebook dentro de la oficina y la notebook fuera de ella, podemos observar que su valor aumenta considerablemente lo que resulta en una conexión "lenta". Por otro lado, si nos alejamos demasiado del router como es el caso de la 2da prueba del inciso 4-h, ya no tenemos recepción de los paquetes debido a que estamos fuera del rango de la red que genera el router.
    Esto nos permite comprobar por medio de una simulación, el fenómeno que hablamos en el punto 1, sobre la atenuacion de la señal a medida que nos alejamos del origen de la misma.

## Referencias

[1] Radio spectrum, https://en.wikipedia.org/wiki/Radio_spectrum
[2] Comunicaciones y Redes de Computadoras, Stallings, 7ma Edición, PEARSON EDUCACIÓN, S. A., Madrid, 2004