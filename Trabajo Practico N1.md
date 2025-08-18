# Trabajo Práctico 1

**Nombres**  
_María Pilar Sabena_
_Mateo Quispe_
_Nicolas De la Mata_  
_Matias J. Costamagna_

**Ethernautas**  

**Facultad de Ciencias Exactas, Físicas y Naturales**  
**Comunicaciones de Datos**
**Profesores**
_Miguel Á. Solinas_
_Santiago M. Henn_
_Facundo Oliva Cuneo_
**Fecha** _Agosto, 2025_

---

### Información de los autores
 
- **Información de contacto**: _matias.costamagna@mi.unc.edu.ar_  

---

### Desarrollo

- 1
    - b 
    Para obtener el valor de la frecuencia, utilizamos la fórmula que relaciona la velocidad a la que viaja una onda con la longitud de dicha onda.
    La longitud de onda $\lambda$ es la distancia que recorre la onda hasta completar un ciclo, lo que en la imagen se indica como 60 [mm] (o $60e^{-3}$ [m]).

    $f [Hz] = \frac{c}{\lambda} = \frac{3e^8 [m/s]}{60e^{-3} [m]} = 5e^9 [Hz] = 5 [GHz]$

    - c
    La onda del punto _a_, tiene una frecuencia de 5 [GHz], por lo que la banda correspondiente que incluye esta frecuencia es la banda Banda de Frecuencia Super Alta (Super High Frequency o SHF), que abarca frecuencias entre 3 [GHz] y 30 [GHz].

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
    Si hablamos de modulaciones de señales analógicas para datos digitales, otras técnicas similares, son la FSK, ASK, QAM y todas sus variantes dependiendo de la cantidad de símbolos distintos que se quieran transmitir [1].

    - d
    El BER es un parámetro que indica que tan bueno es el desempeño de un sistema de comunicación determinado.
    Fundamentalmente indica la probabilidad de error por bit transmitido.
    La técnica de modulación con mejores prestaciones es la PSK, la comparación entre las técnicas y sus eficiencias se encuentra desarrollada en el libro [1].


## Referencias

[1] Comunicaciones y Redes de Computadoras, Stallings, 7ma Edición, PEARSON EDUCACIÓN, S. A., Madrid, 2004