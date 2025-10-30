# Trabajo Práctico 4

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

### Desarrollo

### Punto 1

a) Las redes se clasifican según su cobertura geográfica:
- PAN (Personal Area Network):
    - Alcance: Muy reducido (pocos metros, hasta ~10m)
    - Características: Conecta dispositivos personales cercanos (smartphone, laptop, smartwatch, auriculares)
    - Tecnologías: Bluetooth, NFC, USB

- LAN (Local Area Network):
    - Alcance: Edificio o campus (hasta ~1 km)
    - Características: Red privada de alta velocidad, baja latencia, propiedad de una organización
    - Tecnologías: Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11)

- MAN (Metropolitan Area Network):
    - Alcance: Ciudad o área metropolitana (hasta ~50 km)
    - Características: Interconecta múltiples LANs en una zona geográfica amplia
    - Tecnologías: Fibra óptica, enlaces inalámbricos de alta capacidad

- WAN (Wide Area Network):
    - Alcance: País, continente o mundial
    - Características: Conecta redes a grandes distancias, menor velocidad que LAN/MAN, usa infraestructura de proveedores
    - Tecnologías: MPLS, Frame Relay, Internet 

b) VLAN (Virtual Local Area Network) es una red lógica que permite segmentar una red física (LAN) en múltiples redes virtuales independientes, sin necesidad de cambiar la infraestructura física.
Clasificación de VLANs:

- Por Puerto (Port-based VLAN): Los puertos del switch se asignan manualmente a una VLAN específica
- Por Protocolo (Protocol-based VLAN): Basada en el tipo de protocolo (IP, IPX, AppleTalk)
- Por Dirección MAC (MAC-based VLAN): Asigna dispositivos a VLANs según su dirección MAC
- Por subred IP (Network-based VLAN): Basada en la dirección IP del dispositivo

VLANs especiales:
- VLAN 1: VLAN por defecto, tráfico de gestión
- VLAN nativa: Para tráfico sin etiquetar en enlaces trunk
- VLAN de gestión: Para administración de dispositivos de red

c) EEE 802.1Q es el estándar que define el etiquetado de tramas Ethernet (frame tagging) para implementar VLANs en redes conmutadas. <br>Inserta un campo de 4 bytes en la trama Ethernet (entre los campos de dirección MAC de origen y EtherType).
Este campo contiene:
- TPID (Tag Protocol Identifier): 2 bytes - valor 0x8100
- TCI (Tag Control Information): 2 bytes
    - PCP (3 bits): Prioridad (QoS)
    - DEI (1 bit): Drop Eligible Indicator
    - VID (12 bits): VLAN ID (0-4095)

Relación con VLANs:
- Permite que múltiples VLANs compartan el mismo enlace físico (trunk)
- Los switches usan el VID para identificar a qué VLAN pertenece cada trama
- Mantiene el aislamiento lógico entre VLANs aunque compartan infraestructura

d) El Tagginge es el mecanismo técnico que hace posible la implementación práctica de las VLANs dentro de redes de alcance LAN. En el contexto de la clasificación de redes por alcance, tradicionalmente una LAN física representaba un único dominio de broadcast que requería infraestructura dedicada para cada segmento de red, lo cual era costoso e inflexible. Las VLANs resolvieron este problema permitiendo crear múltiples redes lógicas sobre la misma infraestructura física, pero esto generó un nuevo desafío: cuando múltiples VLANs comparten el mismo enlace físico entre switches, es necesario un método para identificar a qué VLAN pertenece cada trama. El Tagging, definido por el estándar IEEE 802.1Q, soluciona este problema insertando un campo de 4 bytes en las tramas Ethernet que incluye el identificador de VLAN (VID). Este proceso funciona de la siguiente manera: cuando una trama llega a un puerto de acceso, el switch conoce la VLAN asociada a ese puerto; si la trama debe enviarse a través de un enlace trunk hacia otro switch, el switch agrega la etiqueta 802.1Q con el número de VLAN correspondiente; la trama viaja por el cable físico con esta etiqueta, permitiendo que múltiples VLANs compartan el mismo medio; el switch receptor lee la etiqueta, identifica la VLAN y envía la trama solo a los puertos que pertenecen a esa VLAN; finalmente, si el puerto destino es de acceso, se remueve la etiqueta antes de entregar la trama al dispositivo final. De esta forma, el Tagging es la tecnología fundamental que permite virtualizar una única LAN física en múltiples LANs lógicas aisladas, haciendo posible que empresas, campus universitarios o cualquier organización puedan segmentar su red por departamentos, funciones o niveles de seguridad sin necesidad de duplicar la infraestructura física de switches y cableado, optimizando recursos y simplificando la gestión de red.

---

### Punto 2

![Red Topologica](https://hackmd.io/_uploads/r1uL1BuAxl.png)


a) Cambio de nombre de los switches
![2-A-SW1](https://hackmd.io/_uploads/S1cYC4dAxg.png)
![2-A-SW2](https://hackmd.io/_uploads/r1ljRNdRgg.png)

b) Asignacion de contraseñas
![2-B-SW1](https://hackmd.io/_uploads/r13jAVdClg.png)
![2-B-SW2](https://hackmd.io/_uploads/SJhoAVd0gx.png)

c)Encriptacion de contraseñas
![2-C](https://hackmd.io/_uploads/B1C1yruRee.png)

d) Configuracion VLANs
![2-D-SW1](https://hackmd.io/_uploads/ryQ-1B_0gg.png)
![2-D-SW2](https://hackmd.io/_uploads/r1X-Jrd0lx.png)

e) Interfaces activas
![2-E-F-SW1](https://hackmd.io/_uploads/S1sGkHd0le.png)
![2-E-F-SW2](https://hackmd.io/_uploads/S1ozkHORge.png)

g) Comunicacion entre computadoras
![2-G](https://hackmd.io/_uploads/r1fv1SdRgg.png)

h) Creacion VLANs
![2-H-SW1](https://hackmd.io/_uploads/BJDdJHuRxe.png)

i) La VLAN utilizada por defecto es la VLAN 1.
![2-I-SW1](https://hackmd.io/_uploads/SJgnyS_Rll.png)

j) Asignacion de PC-A a VLAN Laboratorio (VLAN 10)
![2-J-SW1](https://hackmd.io/_uploads/B176yruRgg.png)

k) Modificacion IP de VLAN 1 y estado de Interfaces e IP's
![2-K-L-SW1 (2)](https://hackmd.io/_uploads/r1rylrdAgl.png)
![2-K-L-SW1](https://hackmd.io/_uploads/BJrylBuRex.png)

m) Asignacion PC-B a VLAN Laboratorio (VLAN 10)
![2-M-SW2 (2)](https://hackmd.io/_uploads/S1Fzxr_Alx.png)
![2-M-SW2](https://hackmd.io/_uploads/ryYMxS_Axg.png)

n) Verificacion de conexion entre PC's y entre Switches
![2-N-PCA](https://hackmd.io/_uploads/B1hb7gbJbg.png)
![2-N-SW1](https://hackmd.io/_uploads/ByeCmxZybl.png)

--- 

### Punto 3

1. Diseño y Cableado Físico
Se implementó una topología centralizada compuesta por el Router Aircraft, un Switch (SW), un Server Entretenimiento y siete dispositivos finales (PCs).



| Conexión | Dispositivos | Interfaz Router | Interfaz Switch | Tipo de Cable |
| -------- | -------- | -------- | - | - |
| Enlace Troncal     | Router $\leftrightarrow$ SW     | Fa0/0     | F0/1 | Cobre Directo |
| WAN/ISP | Router $\leftrightarrow$ ISP Router | Fa0/1 | G0/0 | Cobre Cruzado |
| Server     | SW $\leftrightarrow$ Server     | N/A     | F0/8 | Cobre Directo |
| PCs Cliente | SW $\leftrightarrow$ PCs | N/A | F0/2 a F0/7 | Cobre Directo |

![Topologico - Punto 3](https://hackmd.io/_uploads/SkOs9Wb1Zx.png)


2. Configuración del Switch (SW)
Se definieron las VLANs y se asignaron los puertos según la clase de servicio.

    A. Creación y Nombres de VLANs
    Se crearon y nombraron las VLANs necesarias:

    Fragmento de código:

    vlan 10
     name Turista
    vlan 20
     name Business
    vlan 99
     name Admin
     
    B. Asignación de Puertos (Access Ports)
Se asignaron los puertos al modo de acceso según el número de PCs por clase:


    | Clase | VLAN | Interfaz(ces) | PCs | 
    | -------- | -------- | -------- | - |
    | Turista     | 10     | FastEthernet0/2 - 4     | 3 |
    | Business     | 20     | FastEthernet0/5 - 6     | 2 |
    | Admin     | 99     | FastEthernet0/7     | 1 |
    | Server     | 99     | FastEthernet0/8     | 1 |
    
    C. Enlace Troncal
Se configuró el puerto F0/1 como troncal para el Router:
    interface FastEthernet0/1
     switchport mode trunk

3. Configuración del Router Aircraft
El Router se configuró para enrutamiento, NAT y aplicación de ACLs, utilizando la sintaxis de interfaces FastEthernet (Fa0/0 y Fa0/1).

    **A. Enrutamiento Inter-VLAN (Subinterfaces):**
Se crearon las subinterfaces en Fa0/0 para actuar como Gateways y se marcaron como interfaces NAT Internal.

    Fragmento de código:

        interface FastEthernet0/0.10
        encapsulation dot1Q 10
        ip address 10.10.10.1 255.255.255.0
        ip nat inside
        interface FastEthernet0/0.20
        encapsulation dot1Q 20
        ip address 10.10.20.1 255.255.255.0
        ip nat inside
        interface FastEthernet0/0.99
        encapsulation dot1Q 99
        ip address 10.10.99.1 255.255.255.0
        ip nat inside

    **B. Interfaz WAN y NAT Outside:**
Se configuró la interfaz de salida a Internet y se marcó como NAT Outside.

    Fragmento de código:

        interface FastEthernet0/1
        ip address 200.0.0.1 255.255.255.252
        ip nat outside
        no shutdown
     
     **C. Configuración de NAT (VLAN 20 Exclusiva):** Se implementó PAT (Port Address Translation) para permitir que solo la VLAN 20 acceda a Internet.

    Fragmento de código:

        access-list 20 permit 10.10.20.0 0.0.0.255
        ip nat inside source list 20 interface FastEthernet0/1 overload
    
    **D. ACL (Restricción de Turista):** Se aplicó la ACL extendida 100 para bloquear el tráfico de Turista (10.10.10.0/24) hacia cualquier destino externo, mientras se permite el tráfico restante (incluido el tráfico interno hacia el servidor).

    Fragmento de código:

        access-list 100 deny ip 10.10.10.0 0.0.0.255 any
        access-list 100 permit ip any any
        interface FastEthernet0/0.10
        ip access-group 100 out
     
     **E. Ruta por Defecto:** Se configuró una ruta estática para dirigir todo el tráfico desconocido (Internet) al ISP:

    Fragmento de código:

        ip route 0.0.0.0 0.0.0.0 200.0.0.2
    
4. Direccionamiento de End Devices y Servidor

    Los dispositivos finales fueron configurados con direcciones IP estáticas y su Gateway correspondiente (la IP de la subinterfaz del router). Por ejemplo, el Server Entretenimiento se configuró con la IP $10.10.99.10$ y Gateway $10.10.99.1$.

5. Pruebas

    A. Ping al servidor de entretenimiento desde PC Turista.
    ![3-A](https://hackmd.io/_uploads/SkpimZZkbl.png)
    
    B. Acceso HTTP a servidor local desde PC Turista.
    ![3-B](https://hackmd.io/_uploads/HkK4EZ-1Wx.png)
    
    C. Ping a Internet desde PC Turista.
    ![3-C](https://hackmd.io/_uploads/S1mv1fZ1be.png)


    D. Acceso HTTP a servidor local desde PC Business.
    ![3-D](https://hackmd.io/_uploads/SyyYSZ-kWe.png)
    
    E. Ping a Internet (ej: 8.8.8.8) desde PC Business.
    ![3-E](https://hackmd.io/_uploads/S1muF--1Zx.png)
    
    F. Ping entre Admin y todos.
    
    Ping a Dispositivos Locales (VLAN 99): Comprueba la conectividad con el Servidor de Entretenimiento, que también está en la VLAN 99.

    ![3-F (1)](https://hackmd.io/_uploads/ryjRtb-yZe.png)
    
    Ping a Otras VLANs: Comprueba la comunicación a través del Router Aircraft a las VLANs de Turista y Business.

    ![3-F (2)](https://hackmd.io/_uploads/S10Q5--1bl.png)
    
    Ping a Internet (Comprobación de Acceso Total): Comprueba si la PC Admin tiene acceso a la red externa simulada por el ISP.

    ![3-F (3)](https://hackmd.io/_uploads/HyBD5WZkZx.png)



### Conclusion

La implementación del Punto 3 logró exitosamente la segmentación y el control de acceso necesarios para simular una red LAN a bordo de una aeronave, cumpliendo con los requisitos de seguridad y servicio diferenciado para cada clase (Turista, Business y Admin).

1. Éxito de la Segmentación y el Enrutamiento
     - Segmentación de Capa 2 (Switch): La creación de las VLANs 10, 20 y 99 y la correcta asignación de los puertos de acceso (incluido el servidor) aseguraron que el tráfico de cada clase estuviera aislado a nivel de capa de enlace.
     - Enrutamiento Inter-VLAN (Router Aircraft): La configuración de subinterfaces en el Router (Fa0/0.10, Fa0/0.20, Fa0/0.99) permitió que la comunicación entre las clases fuera posible, estableciendo los Gateways $10.10.X.1$ necesarios.


2. Validación de las Políticas de Acceso (NAT y ACL)
Las pruebas de conectividad validaron la implementación de las políticas de seguridad:



| Prueba | Resultado | Conclusión |
| -------- | -------- | -------- |
| PC Business $\leftrightarrow$ Internet ($8.8.8.8$)     | Éxito     | Se confirmó que el NAT y la ACL 20 tradujeron correctamente el tráfico de la VLAN 20, permitiendo la navegación.     |
| PC Turista $\leftrightarrow$ Internet ($8.8.8.8$)     | Fallo (Request timed out)     | Se validó que la ACL 100 aplicada de forma saliente (out) en la subinterfaz Fa0/0.10 bloqueó exitosamente el acceso a Internet para la VLAN 10.     |
| PC Turista $\leftrightarrow$ Server ($10.10.99.10$)     | Éxito     | Se comprobó que, a pesar de la ACL, el tráfico interno (Intra-VLAN e Inter-VLAN local) no fue bloqueado, permitiendo el acceso al servidor de entretenimiento.     |
| PC Admin $\leftrightarrow$ Todos     | Éxito     | Se confirmó que la VLAN 99 mantiene un acceso total (sin restricciones de NAT o ACL), tal como se requiere para el segmento de administración.     |

En resumen, la implementación demostró la capacidad del enrutamiento inter-VLAN para segmentar redes y el uso combinado de NAT y ACLs para aplicar políticas de acceso basadas en requisitos específicos del servicio.