# Trabajo Práctico 5

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

**Fecha:** _Noviembre_, 2025_

---

### Desarrollo

### Punto 1
Características principales:

- Protocolo ligero de mensajería diseñado para comunicación máquina a máquina (M2M) e IoT
- Funciona sobre TCP/IP
- Usa el modelo publish/subscribe
- Ofrece tres niveles de QoS (Quality of Service): 0, 1 y 2
- Pequeña huella de código y consumo mínimo de ancho de banda

Ventajas:

- Muy eficiente en redes con ancho de banda limitado
- Bajo consumo de energía (ideal para dispositivos IoT)
- Escalable para miles de clientes
- Soporte de mensajes persistentes
- Desacoplamiento entre publicadores y suscriptores

Desventajas:

- Requiere un broker centralizado (punto único de fallo)
- Seguridad básica en la versión estándar (necesita TLS/SSL adicional)
- No tiene mecanismos nativos de descubrimiento de servicios
- La falta del broker hace que toda la red caiga

Principales usos:

- Sistemas IoT (sensores, actuadores)
- Automatización del hogar
- Telemetría y monitoreo remoto
- Aplicaciones móviles push
- Mensajería instantánea

El patrón Publish/Subscribe (PubSub) es un patrón de diseño de mensajería donde los emisores (publishers) no envían mensajes directamente a receptores específicos (subscribers). En su lugar:
- Los publishers publican mensajes en tópicos sin conocer quién los recibirá
- Los subscribers se suscriben a tópicos de interés sin conocer quién publica
- Un broker central gestiona las suscripciones y distribuye los mensajes
- Hay desacoplamiento total entre publishers y subscribers

Este patrón permite escalabilidad, flexibilidad y comunicación asíncrona entre componentes.

---

### Punto 3

Mensaje enviado desde el Publisher:

![Screenshot 2025-11-14 181228](https://hackmd.io/_uploads/ByqKjMSlZe.png)

Mensaje recibido en el Suscriber:

![Screenshot 2025-11-14 181248](https://hackmd.io/_uploads/HJqYsGrgWe.png)

---

### Punto 4

a) 
Dispositivo A:

![image](https://hackmd.io/_uploads/SyAkk7BxZx.png)

Dispositivo B:

![image](https://hackmd.io/_uploads/HJzbJXHe-l.png)


b)
Receptor 1:

![image](https://hackmd.io/_uploads/B1vtl7rgZx.png)

Receptor 2:

![image](https://hackmd.io/_uploads/r1KulQSlbe.png)

Cliente central:

![image](https://hackmd.io/_uploads/r1Sjg7Be-x.png)

---

### Punto 5

Terminal Gateway:

![image](https://hackmd.io/_uploads/S1r1HQHxWx.png)

Terminal Sensor Temperatura Sala 1:

![image](https://hackmd.io/_uploads/SJ_5r7HxWx.png)

Terminal Sensor Temperatura Sala 2:

![image](https://hackmd.io/_uploads/BkJTrmBlWe.png)

Terminal Sensor Humedad Sala 1:

![image](https://hackmd.io/_uploads/SJk2r7Bg-l.png)

Terminal Panel de control:

![image](https://hackmd.io/_uploads/rJjGS7rl-l.png)

Terminal Gateway funcinonando:

![image](https://hackmd.io/_uploads/SkerSXrgZe.png)

HiveMQ Cloud:

![image](https://hackmd.io/_uploads/ry0ArXBx-l.png)

Panel de control STOP:

![image](https://hackmd.io/_uploads/ByQNUmHlZg.png)

Sensor Temperatura 2 recibiendo el comando:

![image](https://hackmd.io/_uploads/HJUHUmHlWx.png)

Sensor Humedad recibiendo el comando:

![image](https://hackmd.io/_uploads/H1tUU7Hgbe.png)

Sensor Temperatura 1 recibiendo el comando:

![image](https://hackmd.io/_uploads/B1OPUmHgZe.png)

Captura del archivo CSV:

![image](https://hackmd.io/_uploads/SyNiuXHgZe.png)


e) Paquete:
No. | Tiempo |	Fuente |	Destino	|Protocolo|	Longitud	|Info|
|---|---|---|---|---|---|---|
50|	0.220871|	192.168.1.41|	52.31.149.80|	TLSv1.2|	87|	Application Data|

![image](https://hackmd.io/_uploads/Byzfp7re-e.png)

---

### Punto 6

a) En esta actividad, MQTT opera principalmente sobre TCP/IP (Protocolo de Control de Transmisión), utilizando el puerto 8883 para conexiones seguras con TLS/SSL, garantizando una comunicación confiable y orientada a conexión. La eleccion de TCP asegura la entrega ordenada y sin perdida de paquetes, lo cual es fundamental para la mensajeria MQTT.

b)
- Integridad: Garantizada por el checksum de TCP que detecta corrupción de datos, los niveles QoS 1 y 2 implementan acuses de recibo y mecanismos de retransmisión. El broker valida la estructura de los mensajes MQTT según el estándar del protocolo.
- Confidencialidad: Al usar TLS, cifra todo el tráfico entre tu cliente y el broker, protegiendo credenciales y mensajes de ser espiados.
- Disponibilidad: La disponibilidad de todo el sistema depende de que el broker central (HiveMQ Cloud) esté en línea y tener conexión a Internet estable para alcanzarlo. Si el broker se cae, o si la red local pierde conexión a Internet, ningún dispositivo podrá comunicarse.

c) Los niveles de QoS (0, 1, 2) determinan el grado de garantía en la entrega.
- QoS 0:
    - Mensajería "fire and forget" sin acuse de recibo
    - Máximo rendimiento pero posible pérdida de mensajes

- QoS 1:
    - El mensaje se envía y se almacena hasta que el receptor (broker o cliente final) envía una confirmación (PUBACK)
    - Puede generar mensajes duplicados que deben manejarse a nivel aplicación
    - Balance entre fiabilidad y rendimiento para la mayoría de casos

- QoS 2:
    - Protocolo de 4 pasos (PUBLISH → PUBREC → PUBREL → PUBCOMP)
    - Elimina duplicados garantizando entrega exactamente una vez
    - Mayor overhead pero esencial para transacciones críticas

d) Ventajas del modelo pub/sub:
- Desacoplamiento espacial: Los publicadores y suscriptores no necesitan conocerse mutuamente, tampoco requieren direccionamiento directo ni descubrimiento de servicios.

- Desacoplamiento temporal: Los componentes pueden funcionar de forma asíncrona y su mensajería persistente permite la entrega (aunque los suscriptores estén offline).

- Escalabilidad: Su arquitectura one-to-many permite agregar suscriptores sin modificar publicadores y la distribución natural de carga mediante múltiples suscriptores.

- Flexibilidad: Ofrece tópicos jerárquicos que permiten routing lógico complejo, los comodines (#, +) facilitan suscripciones a patrones de mensajes y tiene fácil integración de nuevos componentes sin reconfigurar el sistema existente.

e)  La principal limitación es que MQTT es un protocolo de capa de aplicación que impone un modelo publicador/suscriptor (pub/sub), el cual depende de un broker central. Esto contrasta con el potencial de una red LAN real, que permite una comunicación directa entre dispositivos (por ejemplo, mediante sockets TCP/IP directos).
Esta dependencia obligatoria del broker introduce limitaciones específicas en el contexto de una LAN:
- Punto Único de Falla: Si falla, toda la comunicación MQTT se detiene, incluso si la red LAN subyacente y los dispositivos están perfectamente operativos.

- Latencia y Cuello de Botella: El flujo de mensajes se vuelve Dispositivo A -> Broker -> Dispositivo B. Este salto extra introduce latencia en lugar de una comunicación directa. Además, el broker mismo puede convertirse en un cuello de botella si el tráfico de la red es muy alto.

-  Dependencia de Conectividad Externa: Si el broker está en la nube, la comunicación local dentro de la LAN se vuelve dependiente de una conexión a Internet funcional.

f) Las implicaciones de depender de un broker central para la comunicacion, crea un punto único de falla que puede interrumpir toda la comunicación si falla. Todo el tráfico pasa por este cuello de botella, añadiendo latencia a cada mensaje. Operativamente requiere mantenimiento constante y genera costos adicionales. En seguridad, concentra el riesgo de ataques y da acceso centralizado a todos los mensajes. La recuperación ante fallos es compleja y puede causar pérdida de mensajes sin mecanismos de persistencia adecuados.