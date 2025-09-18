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

        \[
        n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)
        \]

        donde:  
        - \(n_1\) y \(n_2\) son los índices de refracción de los medios,  
        - \(\theta_1\) es el ángulo de incidencia,  
        - \(\theta_2\) es el ángulo de refracción.  

        En el caso de la **fibra óptica**, esta ley explica el fenómeno de la **reflexión interna total**, que ocurre cuando la luz pasa del núcleo (con mayor índice de refracción) al revestimiento (con menor índice de refracción) en un ángulo mayor al **ángulo crítico**. Esto asegura que la señal se mantenga confinada dentro del núcleo y se propague a lo largo de la fibra.  

        La relación con los **modos de transmisión** es la siguiente:  
        - En **fibra monomodo**, el núcleo es muy pequeño y solo se permite un camino de propagación, minimizando la dispersión.  
        - En **fibra multimodo**, el núcleo es mayor y la luz puede reflejarse en múltiples trayectorias, lo que genera dispersión modal y limita la distancia máxima de transmisión.  