# Trabajo Práctico 3

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

**Fecha:** _Septiembre_, 2025_

---

### Introducción

---

### Desarrollo

- 1

    - a) Historia y campo de aplicación de los estándares IEEE 802.3 y 802.11

        El estándar IEEE 802.3, conocido comúnmente como Ethernet, fue publicado en 1983 con el objetivo de definir las especificaciones de la capa física y de la subcapa de control de acceso al medio (MAC) para redes de área local cableadas. A lo largo de los años ha evolucionado desde las primeras versiones que ofrecían 10 Mbps de velocidad hasta las implementaciones actuales que superan los 400 Gbps, siendo la base de la gran mayoría de las redes LAN en el mundo. Su campo de aplicación principal es la transmisión de datos mediante cableado (UTP, STP o fibra óptica), garantizando alta velocidad, estabilidad y baja latencia.

         Por otro lado, el estándar IEEE 802.11, publicado en 1997, corresponde a las redes de área local inalámbricas, conocidas como Wi-Fi. Este estándar define también la capa física y la subcapa MAC, pero orientadas a la transmisión por medios inalámbricos utilizando radiofrecuencia. Desde su primera versión, con velocidades modestas (2 Mbps), ha ido evolucionando en distintas versiones como 802.11a/b/g/n/ac/ax hasta la más reciente 802.11be, alcanzando velocidades del orden de los gigabits por segundo. Su campo de aplicación se centra en las redes WLAN, brindando movilidad, facilidad de despliegue y conectividad en entornos donde no es posible o no resulta conveniente el uso de cableado físico.
    - c) Cuando una red Wi-Fi opera con un determinado protocolo (por ejemplo, 802.11ax – Wi-Fi 6) y un dispositivo posee una placa de red inalámbrica (NIC) más antigua que no soporta dicho protocolo, pueden ocurrir dos situaciones:

        Compatibilidad descendente (backward compatibility): en la mayoría de los casos, los puntos de acceso Wi-Fi son retrocompatibles. Esto significa que el dispositivo podrá conectarse, pero utilizando la versión más antigua que ambos soporten. Por ejemplo, si la red está en Wi-Fi 6 y la notebook solo soporta Wi-Fi 4 (802.11n), la conexión se establecerá bajo 802.11n, con menor velocidad y eficiencia.

        Incompatibilidad total: si el punto de acceso no admite protocolos anteriores o la NIC es demasiado antigua para reconocer el estándar, la conexión no será posible. Esto puede ocurrir con equipos muy viejos frente a protocolos modernos.

        En síntesis, lo usual es que la red se degrade a la versión común más baja soportada, afectando el rendimiento, la seguridad y la experiencia de usuario, pero manteniendo la conectividad.
    - e) 

| Característica        | Wi-Fi 5              | Wi-Fi 6              | Wi-Fi 7               |
|------------------------|----------------------|----------------------|-----------------------|
| Versión IEEE           | 802.11ac             | 802.11ax             | 802.11be              |
| Tasa de datos máxima   | ~6,9 Gbps            | ~9,6 Gbps            | ~46 Gbps              |
| Bandas                 | 5 GHz                | 2,4 / 5 / 6 GHz      | 2,4 / 5 / 6 GHz       |
| Ancho de banda         | 20 – 160 MHz         | 20 – 160 MHz         | hasta 320 MHz         |
| Modulación             | 256-QAM              | 1024-QAM             | 4096-QAM              |
| Sistema de Seguridad   | WPA2                 | WPA3                 | WPA3      |
  
- 2

    a) – Tipos de transmisión en Fibra Óptica

    En la figura se ilustran dos tipos de transmisión:

    #### 1. Fibra Monomodo (izquierda)
    - La luz viaja en un único camino recto por el núcleo.  
    - Núcleo muy delgado (≈ 8–10 µm).  
    - Permite grandes distancias (decenas o cientos de km) con baja atenuación.  
    - Gran ancho de banda y velocidad de transmisión.  
    - Más costosa de implementar (requiere láseres precisos y conectores delicados).

    #### 2. Fibra Multimodo (derecha)
    - La luz se propaga en múltiples trayectorias (rebotes en el núcleo).  
    - Núcleo más ancho (≈ 50–62,5 µm).  
    - Más económica y sencilla de instalar (usa LEDs como fuente de luz).  
    - Adecuada para distancias cortas (hasta algunos km).  
    - Presenta dispersión modal que limita velocidad y alcance.

    b) Ley de Snell y su relación con la Fibra Óptica  

        La **Ley de Snell** establece la relación entre los ángulos de incidencia y refracción de un rayo de luz cuando pasa de un medio a otro con distinto índice de refracción. Su expresión matemática es:  


    $    n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)$

        donde:  
    $ n_1 y n_2$ son los índices de refracción de los medios,  
    $ theta_1 $ es el ángulo de incidencia,  
    $theta_2 $ es el ángulo de refracción.  

        En el caso de la **fibra óptica**, esta ley explica el fenómeno de la **reflexión interna total**, que ocurre cuando la luz pasa del núcleo (con mayor índice de refracción) al revestimiento (con menor índice de refracción) en un ángulo mayor al **ángulo crítico**. Esto asegura que la señal se mantenga confinada dentro del núcleo y se propague a lo largo de la fibra.  

        La relación con los **modos de transmisión** es la siguiente:  
        - En **fibra monomodo**, el núcleo es muy pequeño y solo se permite un camino de propagación, minimizando la dispersión.  
        - En **fibra multimodo**, el núcleo es mayor y la luz puede reflejarse en múltiples trayectorias, lo que genera dispersión modal y limita la distancia máxima de transmisión.  
- 3 
    - a

| Protocolo | ¿Está estandarizado? Si/No | Si aplica: ¿Cuál(es) estándares? (si tiene varios mencionar la última versión) |
|-----------|----------------------------|--------------------------------------------------------------------------------|
| Wi-Fi     | Sí                         | IEEE 802.11 (última versión: 802.11ax – Wi-Fi 6/6E, en desarrollo 802.11be – Wi-Fi 7) |
| Bluetooth | Sí                         | IEEE 802.15.1 / Bluetooth SIG (última versión: Bluetooth 5.4, 2023)            |
| ZigBee    | Sí                         | IEEE 802.15.4 + ZigBee Alliance (última versión: ZigBee 3.0)                   |
| NFC       | Sí                         | ISO/IEC 18092, 21481, ECMA-340 (última versión soportada: NFC Forum standards) |
| LTE       | Sí                         | 3GPP Release 8 en adelante (última evolución: LTE-Advanced Pro, Rel. 13–15)    |
| GSM       | Sí                         | 3GPP Release (Rel. 99 y sucesivas, aunque en desuso)                           |
| 5G (3GPP) | Sí                         | 3GPP Release 15, 16, 17 (última versión: Rel. 17 aprobada en 2022, avanzando a Rel. 18) |
| LoRa      | Parcialmente               | LoRa propietario (Semtech) + LoRaWAN estandarizado por LoRa Alliance (última versión: LoRaWAN 1.0.4 / 1.1) |
| NB-IoT    | Sí                         | 3GPP Release 13 (parte de LTE evolutivo)                                       |
| SigFox    | No (propietario)           | Tecnología propietaria de SigFox                                               |
| Z-Wave    | Sí (recientemente)         | Z-Wave Alliance, desde 2020 estándar ITU-T G.9959                               |

    El 3GPP (3rd Generation Partnership Project) es el organismo que define los estándares de telecomunicaciones móviles (2G, 3G, 4G, 5G y ahora 6G).


    - c)
    
| Característica                  | UTP                           | Fibra Óptica                         | Wi-Fi 802.11be (Wi-Fi 7)                 | Bluetooth 5.4                 | 5G                                |
|---------------------------------|-------------------------------|--------------------------------------|------------------------------------------|--------------------------------|-----------------------------------|
| **Ancho de banda**              | Hasta 10 Gbps (Cat 6a/7)      | >100 Gbps                            | Hasta 46 Gbps teóricos                   | ~2 Mbps (BLE), hasta 24 Mbps EDR | Hasta 10 Gbps (teórico)           |
| **Distancias**                  | 100 m máx.                   | Varios km (hasta 40 km o más)        | 30–100 m                                | 1–100 m                        | 1–10 km (dependiendo del despliegue) |
| **Inmunidad a EMI / RFI**       | Baja (susceptible a interfer.)| Muy alta (no conductor eléctrico)    | Media (afectado por interferencias)      | Media-baja (interferencias 2.4 GHz) | Media (afectado por condiciones del espectro) |
| **Costos de medios/conectores/dispositivos** | Bajo                          | Alto                                 | Medio                                   | Muy bajo                       | Alto (infraestructura y equipos)   |
| **¿Disponible en Packet Tracer?** | Sí                           | No                                   | Sí                                      | No                             | No                                |

- 4 Estado del arte: conectividad a Internet en vuelos

Qué significa "estado del arte"
El estado del arte (state of the art) es la descripción de las técnicas, tecnologías y resultados más avanzados y recientes en un área determinada. En este apartado se resume qué soluciones actuales existen para ofrecer Internet a aeronaves, qué limitaciones presentan y qué líneas de investigación o despliegue están dominando el mercado.

a) ¿Qué tecnologías permiten conectarse a Internet en un avión? Principales características y limitaciones

Las soluciones usadas hoy en día para proporcionar conectividad a pasajeros en vuelo pueden agruparse en dos grandes familias (y sus variantes):

1. Satcom (conexión vía satélite)

Subtipos / bandas: GEO (geostacionario), MEO (órbita media), LEO (órbita baja); frecuencias típicas: L-band, Ku-band, Ka-band.
Cómo funciona (resumen técnico): la antena del avión (terminal SATCOM, frecuentemente “emergent / phased-array” o antena rotativa/conic) enlaza con satélites que a su vez enrutan tráfico hacia gateways en tierra / backbone. En el avión se proporciona Wi-Fi local (pico-celda interna) y se multiplexa el tráfico de pasajeros por la conexión satelital.
Características:

Cobertura: global (especialmente con constelaciones LEO cuando estén desplegadas).

Velocidades: varían mucho según la constelación y banda: GEO/Ku/Ka con HTS (High Throughput Satellite) pueden ofrecer decenas o cientos de Mbps agregados; LEO recientes prometen latencias y throughput mejores (ej. decenas a centenas Mbps por aeronave en algunos despliegues). 

Latencia: GEO ~500 ms ida-vuelta (alto), LEO típicamente <100 ms (mucho mejor). 
worldaviationfestival.com

Limitaciones: coste de terminales/antenas, consumo energético, aprobaciones y certificación (STC), gestión de handover entre satélites/operadores, contención de capacidad (bandwidth compartida entre usuarios del avión) y posibles interferencias con radio aeronáutica (problemas de integración y certificación). 

2. Air-to-Ground (A2G / ATG)

Cómo funciona: estaciones terrestres (torres A2G) que ofrecen cobertura en rutas donde hay infraestructura en tierra; el avión establece enlaces punto-a-multipunto con estas estaciones (a menudo en bandas tropo-propagadas).
Características:

Latencia: baja (similar a redes celulares).

Velocidad: puede ser elevada pero limitada a la densidad de estaciones y geometría de antenas.

Limitaciones: cobertura limitada sobre océanos/zonas remotas; requiere despliegue terrestre denso. Algunos proveedores combinan ATG + satélite para cubrir zonas sin infraestructura. 

3. Híbridos multi-orbita / multi-banda

Soluciones modernas mezclan varios enlaces (LEO + GEO/Ku/Ka + ATG) y hacen link aggregation / conmutación entre enlaces según disponibilidad, latencia y costo. Este modelo reduce puntos ciegos y mejora experiencia. Varias aerolíneas/operadores y fabricantes impulsan terminales “multi-band / multi-orbit” para poder trabajar con varios proveedores. 
4. Red local de a bordo (IFEC: In-Flight Entertainment & Connectivity)

Dentro del avión se implementa una red local (LAN/WLAN) que incluye: servidores de contenido para entretenimiento a bordo (onboard content server), puntos de acceso Wi-Fi, switch y gateway que conecta con el enlace satelital/ATG. El tráfico de la LAN se divide internamente entre: (i) tráfico local que nunca sale del avión (VOD, catálogo multimedia, mapas), y (ii) tráfico a Internet que se encamina a través de la uplink satelital o ATG. 

Comparación resumida (desde la perspectiva de Comunicaciones de Datos)

Ancho de banda agregado: SATCOM HTS/LEO > ATG (depende del despliegue). LEO tiende a ofrecer mejores tasas por usuario en muchos escenarios recientes. 

Latencia: ATG < LEO < GEO. LEO y nuevas arquitecturas 5G-backhaul espacial buscan latencias aptas para videoconferencia. 

Disponibilidad: SATCOM (global) > ATG (continental) — pero SATCOM requiere terminal certificado por aeronave y acuerdo con proveedor.

Costo: terminal + ancho de banda SATCOM suele ser alto (pero cae con LEO/escala); ATG suele ser más barato por bit en zonas cubiertas. 

b) Publicación reciente (≤ 1 año) localizada y breve resumen

Referencia seleccionada (ejemplo de publicación/estudio reciente):

Enabling Continuous 5G Connectivity in Aircraft through LEO satellites — preprint en arXiv, Apr 9, 2025.
Resumen: estudio sobre viabilidad y estrategias de despliegue para ofrecer conectividad 5G end-to-end basada en constelaciones LEO hacia aeronaves. Analiza problemas de handover dinámico, latencia de ruteo entre gateways, requisitos de terminales a bordo y propuesta de técnicas para mejorar la estabilidad del enlace (beam tracking, handoff anticipado). El artículo demuestra que LEO+5G puede proporcionar experiencia próxima a redes terrestres si se optimizan protocolos de control y buffering. 
arXiv

(Otras fuentes complementarias de 2024–2025: whitepapers de proveedores y reportes de la industria que muestran adopción LEO/Ka/Ku y casos de despliegue de Starlink/Kuiper; por ejemplo Gogo, Viasat, artículos de Runway Girl Network y The Verge sobre acuerdos comerciales recientes). 

Si necesitás la referencia bibliográfica completa (formato APA/IEEE) o el PDF del preprint para adjuntar al informe, te lo traigo y lo incluyo.

c) División del tráfico: contenido a bordo (local) vs tráfico a Internet — ¿cómo se gestiona?
Modelo operativo habitual (arquitectura lógica)

Servidor local a bordo (onboard content server / cache)

Almacena películas, series, mapas, menús, etc.

Servido por la red interna (no pasa por el enlace satelital).

Ventaja: cero consumo del link satelital y muy baja latencia para reproducción (mejor QoE).

Gateway/NAT y uplink (SATCOM o ATG)

Todo tráfico con destino a Internet atraviesa el router/gateway que conecta con el enlace en vuelo.

El proveedor puede aplicar políticas QoS, limitación de ancho de banda por pasajero, o tarificación por sesión/datos.

Captive portal / autenticación / billing

Cuando un usuario se conecta al Wi-Fi, se le redirige a un portal que puede distinguir entre: acceso gratuito al contenido local vs. acceso a Internet (de pago).

El captive portal aplica reglas de enrutamiento para que las URLs/requests hacia contenido local no pasen por la WAN.

Comparación de tráfico (ejemplos prácticos)

Ver una película alojada en el servidor del avión:

Tráfico = local L2/L3 dentro del avión; no consume enlace satelital. El flujo será típico HTTP/HTTPS o streaming local (DLNA/HTTP), baja latencia, alta estabilidad (si el servidor y Wi-Fi local tienen capacidad).

Ver la misma película por streaming desde Internet (Netflix, YouTube):

Tráfico = múltiple Mbps por usuario saliendo por el enlace satelital; puede saturar el enlace y generar buffering/latencia alta para todos. Por eso los operadores prefieren ofrecer onboard VOD o caches.

Enviar/recibir un correo electrónico:

Mucho menos exigente en ancho de banda; es tráfico bidireccional pero esruption eficiente y suele priorizarse (baja ocupación). Un correo simple es trivial comparado con streaming.

Mecanismos de control habituales

Segmentación por VLANs / ACLs: separar SSID/VLAN para pasajeros (pago vs gratuito), operaciones/crew, y sistemas críticos (aviónica y mantenimiento).

Políticas QoS & traffic shaping: prioridad a voz/VoIP y tráfico de control, limitación de streaming a Internet, racionamiento por sesión o por paquete.

Onboard caching / CDN local: entrega de contenido sin tocar el enlace; actualización de catálogo en tierra cuando el avión aterriza o durante ventanas de alta capacidad. 

Proxy / transparent caching / split tunneling: muchas plataformas usan un proxy que decide qué trafico salir al WAN y qué servir localmente.

Billing & captive portal: integración con sistemas de facturación que permiten distintos planes (gratuito con anuncios, pago por velocidad, etc.). 
The Verge
+1

d) Ideas para simular esto en Packet Tracer (cómo dividir tráfico local vs Internet)

Packet Tracer no emula satélites nativamente, pero puedes aproximar la arquitectura y el comportamiento de la red a bordo:

Elementos y topología sugerida (approx):

Server (ContentServer) en la LAN del avión — contiene los ficheros/streams (HTTP server).

Access Point (AP) o varios APs para simular el Wi-Fi de cabina (SSID para pasajeros).

Switch/Cabin Router conectando APs y servidor.

Router / Cloud que representa el uplink hacia Internet. Conecta el router del avión al “Cloud (Internet)” y luego a un servidor externo.

Enlace WAN limitado: en las propiedades del enlace serial/PPP o del enlace WAN que une router a cloud, puedes fijar bandwidth muy bajo y delay alto para simular un enlace satelital (por ejemplo: bandwidth 10 Mbps, delay 200 ms, o 500 ms para GEO). Packet Tracer permite configurar bandwidth en enlaces WAN o usar "Cloud" + "Link" con parámetros.

Captive portal: simular con servidor web que redirige clientes al portal; reglas de Firewall/ACL en el router para permitir tráfico local al ContentServer sin pasar por el uplink, mientras que todo lo demás es NAT/masquerade hacia el cloud.

QoS / traffic shaping: usar colas/queues o ACLs para priorizar tráfico de correo/VoIP y limitar HTTPS streaming hacia el uplink. (Packet Tracer permite configurar políticas básicas de QoS y policers en algunos routers).

Generadores de tráfico: usar varias PCs/hosts que soliciten contenido local (HTTP hacia el ContentServer) y otra parte que descargue de Internet (HTTP a servidores remotos) para observar congestión y latencia.

Pasos concretos (guía rápida)

Crear LAN: switch + AP + ContentServer + varios hosts (pasajeros).

Router del avión: interfaz LAN hacia switch; interfaz WAN hacia Cloud. Configurar NAT/PAT.

Servidor Internet: en la nube, varios servidores para simular streaming externo.

Configuración del enlace WAN: en el router del avión, en la interfaz serial/serial-DCE o en la configuración del enlace, fijar bandwidth y delay para representar satélite (ej. 20 Mbps, 250 ms RTT).

Captive portal: configurar el ContentServer para redirigir a http://portal cuando un host nuevo se conecta; crear reglas en router para permitir tráfico directo a ContentServer sin NAT.

Simulación y medición: generar descargas simultáneas desde: (a) contenido local; (b) contenido remoto. Medir latencia y throughput desde las PC y observar congestión en la WAN.

Ops avanzadas: configurar colas/políticas para limitar streaming a Internet (por ej. policer 2 Mbps por usuario), y monitorizar cómo la reproducción local no se ve afectada.

Nota: Packet Tracer tiene limitaciones (no contiene terminales SATCOM reales ni configuración física de antenas). Para simulaciones más realistas de SATCOM/handovers y beam-tracking convendría usar NS-3, OMNeT++/INET o herramientas específicas de satcom que modelan dinámica LEO/GEO.

e) Recomendaciones y conclusiones para el informe

Tendencia dominante: el mercado está migrando hacia modelos multi-orbit / multi-band con uso intensivo de constelaciones LEO (Starlink, Kuiper, OneWeb, Telesat Lightspeed), porque ofrecen mejor latencia y escalabilidad para tráfico en vuelo. 
worldaviationfestival.com
+1

Mejor práctica operativa: siempre combinar onboard caching (VOD) + captive portal + políticas QoS para garantizar experiencia aceptable a todos los pasajeros y contener costos operativos (las descargas masivas por Internet distorsionan la experiencia). 
https://www.gogoair.com/

Riesgos: integración con radio aeronáutica y certificaciones, coste de ancho de banda satelital, problemas de seguridad (segmentar avionic/ops y pasajero). Ejemplos reales recientes muestran despliegues de Starlink en aerolíneas y algunos incidentes de compatibilidad que deben investigarse durante certificación. 
The Verge
+1

f) Referencias seleccionadas (lectura / citas recomendadas)

Enabling Continuous 5G Connectivity in Aircraft through LEO satellites, preprint arXiv, Apr 9, 2025. 
arXiv

Gogo, A Layered Approach to Provide Truly Global Inflight Connectivity (white paper), Apr 21, 2025. 
https://www.gogoair.com/

The Verge, United Airlines is adding free Starlink Wi-Fi to all of its planes, 13 Sep 2024 (ejemplo de adopción comercial y cifras de performance anunciadas). 
The Verge

Runway Girl Network & industry reports — artículos sobre desempeño y despliegue de LEO/Ka/Ku en aviación (varios 2024–2025). 