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