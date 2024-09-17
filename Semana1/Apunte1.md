# Laboratorio de Lenguajes

## Clase 1: 12/08/2024

**Temas**:  
- Evaluación de los lenguajes de programación a través de las características del software que producen.  
- Principios de diseño de los lenguajes.

## Índice de Contenidos
 - [Introducción](#introducción)
   - [Definición de Lenguaje de Programación](#definición-de-lenguaje-de-programación)
   - [Estructura de un Lenguaje de Programación](#estructura-de-un-lenguaje-de-programación)
 - [Conceptos](#conceptos)
 - [Intérpretes](#intérpretes)
 - [Compiladores](#compiladores)
 - [Antecedentes Históricos](#antecedentes-históricos)
 - [Principios de Diseño](#principios-de-diseño)
 - [Clasificación de los Lenguajes de Programación](#clasificación-de-los-lenguajes-de-programación)
    - [Según el Nivel de Abstracción](#según-el-nivel-de-abstracción)
    - [Según la Forma de Ejecución](#según-la-forma-de-ejecución)
    - [Clasificación según el Paradigma de Programación](#clasificación-según-el-paradigma-de-programación)
  - [Componentes de los Lenguajes de Programación](#componentes-de-los-lenguajes-de-programación)
    - [Componentes Generales de un Lenguaje de Programación](#componentes-generales-de-un-lenguaje-de-programación)
    - [Tipos y Estructuras de Datos](#tipos-y-estructuras-de-datos)

---

### Introducción

En los últimos años, los lenguajes de programación han evolucionado en el desarrollo de software, con el objetivo principal de facilitar al usuario las actividades que realiza día a día. Por este motivo, es importante conocer los conceptos básicos de programación, los tipos de lenguajes que se utilizan para el desarrollo de software, y su funcionamiento para la interpretación de algoritmos, así como para dar solución a los problemas que pudieran presentarse.

### Definición de Lenguaje de Programación

Un **lenguaje de programación** es un conjunto de símbolos y reglas sintácticas y semánticas que definen su estructura y el significado de sus elementos y expresiones. Es utilizado para controlar el comportamiento físico y lógico de una máquina.

Permite especificar de manera precisa:
- Sobre qué datos debe operar una computadora.
- Cómo estos datos deben ser almacenados o transmitidos.
- Qué acciones debe tomar bajo una variada gama de circunstancias.

Todo esto se realiza a través de un lenguaje que intenta estar relativamente próximo al lenguaje humano o natural.

### Funcionalidad y Uso

En términos generales, un lenguaje de programación es una herramienta que permite desarrollar software o programas para computadora. Los lenguajes de programación son empleados para:
- Diseñar e implementar programas encargados de definir y administrar el comportamiento de los dispositivos físicos y lógicos de una computadora.

Esto se logra mediante la creación e implementación de **algoritmos**, que funcionan como una forma de comunicación entre el ser humano y la computadora.

### Estructura de un Lenguaje de Programación

Un lenguaje de programación se conforma de:
- **Símbolos**.
- **Reglas de sintaxis** y **semántica**.

Estas reglas y símbolos definen la estructura principal del lenguaje y le dan un significado a sus elementos y expresiones.

---

> _“Los lenguajes de programación son herramientas clave en la creación de software que automatiza y resuelve problemas del mundo real.”_

---

### Conceptos

- **Sintaxis**: Se define como el conjunto de reglas que deben seguirse al escribir los programas en un lenguaje de programación.
- **Semántica**: Refleja el significado, sentido o interpretación de un lenguaje.
- **Algoritmo**: Es un conjunto finito de instrucciones para llevar a cabo una tarea. Consta de un número finito de pasos, no debe ser ambiguo y debe tener una finalidad o propósito.

La función principal de los lenguajes de programación es escribir programas que permiten la comunicación usuario-máquina. Unos programas especiales (compiladores o intérpretes) convierten las instrucciones escritas en código fuente en instrucciones de lenguaje de máquina (0 y 1).

### Intérpretes

Un **intérprete** es un programa que analiza y ejecuta un código fuente, toma un código, lo traduce y a continuación lo ejecuta.  
**Ejemplos**: PHP, Perl y Python son lenguajes interpretados.

![image](https://github.com/user-attachments/assets/001f57f8-612f-4ca7-a745-97314294764a)

### Compiladores

Un **compilador** es un programa (o conjunto de programas) que traduce un programa escrito en código fuente, generando un programa en código objeto (proceso conocido como compilación). Después, al código objeto se le agregan las librerías a través de un programa (linker) y finalmente, se obtiene el código ejecutable.  
**Ejemplos**: C, C++ y Visual Basic son lenguajes que utilizan un compilador.

### Fases de Compilación

La compilación permite crear un programa de computadora que puede ser ejecutado y comprende tres pasos principales:

1. **Creacion de codigo fuente**
2. **Compilacion del programa**
3. **Enlace del prgrama con las funciones necesarias de la biblioteca**

### Diferencias entre Compiladores e Intérpretes

- Los **compiladores** realizan la traducción en tiempo de desarrollo. El compilador recibe todo el código fuente, lo analiza, optimiza y traduce a lenguaje de máquina, dejando un programa completo listo para su ejecución.
- Los **intérpretes** realizan la traducción en tiempo de ejecución, es decir, a medida que el programa se va ejecutando, el intérprete traduce instrucciones a lenguaje de máquina.

---

## Antecedentes Históricos

El profesor de Matemática e Inventor en la Universidad de Cambridge, Inglaterra, a mediados del siglo XIX, **Charles Babbage** fue el primero en concebir la idea de un lenguaje de programación, al predecir varias de las teorías en las que se basan las computadoras actuales.

### Charles Babbage y Ada Lovelace

Babbage desarrolló la idea de una **máquina analítica programable** que, por limitaciones tecnológicas de su época, no pudo ser construida. Junto con él, su colaboradora **Ada Lovelace** es considerada como la primera programadora de la historia, ya que escribió los primeros programas para la máquina de Babbage utilizando tarjetas perforadas. Estas técnicas fueron seguidas por los primeros programadores de computadoras.

### Evolución de los Lenguajes de Programación

1. **1946** - **Konrad Zuse**, ingeniero alemán, desarrolló el lenguaje **Plankalkül**, utilizado para jugar al ajedrez.
2. **1949** - Surgió el **Short Code**, primer lenguaje aplicado en un dispositivo de cómputo electrónico.
3. **1951** - **Grace Hopper**, trabajando para Remington Rand, diseñó el primer compilador conocido ampliamente, el **A-0**, liberado como **MATH-MATIC** en 1957.
4. **1952** - **Alick E. Glennie** concibió el sistema de programación llamado **Autocode**, un compilador rudimentario.
5. **1957** - Apareció **Fortran** (Formula Translating), creado por un equipo comandado por **John Backus**. Este lenguaje introdujo el uso del compilador y contribuyó en el desarrollo del compilador para **Algol** y la notación **BNF** (Backus Naur Form).

### Lenguajes de Programación en la Actualidad

Durante la década de 1960, comenzaron a aparecer nuevos lenguajes de programación más completos, concebidos con diferentes enfoques, características y propósitos. Actualmente, existen más de dos mil lenguajes de programación y continuamente se crean otros que emplean de forma más eficiente los recursos de las computadoras, facilitando la tarea de programación para los usuarios.

# Principios de diseño

Al diseñar lenguajes de programación, a veces es necesario tomar decisiones sobre:
- Las características que se incluyen de forma permanente.
- Las características que no se incluyen, pero tienen mecanismos que facilitan su inclusión.
- Y, las características que no se permiten.

Estas decisiones pueden afectar al diseño final del lenguaje y en ocasiones entrar en conflicto con otros aspectos del lenguaje.

A continuación, veremos una serie de características deseables de los lenguajes de programación:

- Casi siempre, lograr una de ellas nos acerca a otras características relacionadas, pero inevitablemente también nos aleja de otras características contrapuestas a la primera.
- Cada diseño de un lenguaje supone un compromiso o equilibrio entre las características deseables.

## Resumen de algunos principios de diseño de los lenguajes de programación

### Concisión Notacional
El lenguaje proporciona un marco conceptual para pensar algoritmos y expresar dichos algoritmos con el nivel de detalle adecuado. El lenguaje debe ser una ayuda al programador, proporcionando un conjunto de conceptos claro, simple y unificado. La sintaxis debe ser legible por el programador (o por otras personas que vayan a utilizar esos programas).

En otras palabras, el lenguaje debe permitir:
- **Fácil escritura**: facilidad para expresar un cálculo de forma clara, correcta, concisa, y rápida.
- **Legibilidad**: el diseño del lenguaje debe permitir que la lectura de los programas lleve fácilmente a una comprensión correcta del cálculo que significan.

### Ortogonalidad
Dos características de un lenguaje son ortogonales si pueden ser comprendidas y combinadas de forma independiente. La ortogonalidad ofrece la posibilidad de combinar características de todas las formas posibles (sin excepciones). La falta de ortogonalidad puede suponer la enumeración de situaciones excepcionales o la aparición de incoherencias.

En otras palabras, las diferentes características deben ser lo más independientes posible entre ellas.

### Abstracción
El lenguaje debe evitar forzar a los programadores a tener que enunciar algo más de una vez. Ejemplos de técnicas de abstracción son los procedimientos y funciones, la genericidad, y los patrones de diseño.

### Seguridad
La fiabilidad de los productos software es cada vez más importante. Lo ideal es que los programas incorrectos no pertenezcan al lenguaje y sean rechazados por el compilador.

### Expresividad
El programador debe poder expresar sus intenciones. En ocasiones, demasiada expresividad puede implicar falta de seguridad.

### Extensibilidad
El lenguaje debe facilitar mecanismos para que el programador pueda aumentar la capacidad expresiva del lenguaje incorporando nuevas construcciones.

### Portabilidad
El lenguaje debe facilitar la creación de programas que funcionen en el mayor número de entornos computacionales.

### Eficiencia
El programador debe poder expresar algoritmos suficientemente eficientes o el lenguaje debe incorporar técnicas de optimización de los programas escritos en él.

- **Eficiencia en la traducción**: facilidad para construir traductores e intérpretes eficientes.
- **Eficiencia de ejecución**: evitar que la interpretación o ejecución de los programas sea costosa en tiempo o memoria.

### Librerías e Interacción con el exterior
La inclusión de un conjunto de librerías facilita el desarrollo rápido de aplicaciones.

### Entorno
El entorno de desarrollo puede influir en la popularidad de un lenguaje, aunque no sea parte del mismo.

---

## Clasificación de los lenguajes de programación

### Según el nivel de abstracción
- **Lenguaje de Máquina**: Código interpretable directamente por el microprocesador de una computadora.
- **Lenguajes de Bajo Nivel**: Ofrecen poca o ninguna abstracción del hardware, como el lenguaje ensamblador.
- **Lenguajes de Medio Nivel**: Como C, que tiene características de bajo nivel pero con sintaxis de alto nivel.
- **Lenguajes de Alto Nivel**: Como Java, C++ y Python, que permiten codificar algoritmos de manera más natural.

### Según la forma de ejecución
- **Lenguajes Compilados**: El código fuente es traducido a lenguaje máquina antes de ser ejecutado.
- **Lenguajes Interpretados**: El código fuente es traducido e interpretado durante la ejecución.

#### Diferencias entre lenguajes compilados e interpretados
- Los compiladores traducen todo el programa de una vez, mientras que los intérpretes lo hacen línea por línea.
- Los lenguajes compilados suelen ser más eficientes en tiempo de ejecución.
- Los lenguajes interpretados son más portables, ya que solo necesitan un intérprete para funcionar en diferentes arquitecturas.

### Clasificación según el paradigma de programación
- **Imperativo**: Describe programas como un conjunto de instrucciones que cambian el estado del programa.
- **Declarativo**: Se basa en predicados lógicos o funciones matemáticas, enfocándose en qué problema resolver, no en cómo.
- **Orientado a Objetos**: Usa objetos y sus interacciones para diseñar aplicaciones, basado en conceptos como herencia, modularidad, polimorfismo y encapsulamiento.

---

## Componentes de los Lenguajes de Programación

Los lenguajes de programación no han dejado de ser un conjunto de símbolos con una estructura gramatical, reglas semánticas y de sintaxis. Los lenguajes de alto nivel han facilitado su uso al implementar un lenguaje parecido al inglés, más reducido y formal, para establecer condiciones como `if-then-else`, indicar el tipo de dato que se va a manejar como `integer`, `real`, `double`, o señalar eventos como `print`. También hay signos y operadores que ayudan a estructurar operaciones matemáticas o lógicas, como suma, resta, multiplicación (`+`, `-`, `*`, `/`), etc.

## Componentes Generales de un Lenguaje de Programación

### 1. Tipos y Estructuras de Datos
Las estructuras de datos son elementos que permiten manipular de forma más eficiente variables diversas: numéricas, de tipo texto (cadenas de caracteres), y otras más complejas como vectores, matrices y punteros.

### 2. Instrucciones
Son estructuras gramaticales predefinidas, similares al lenguaje humano, que generan secuencias de acciones que conforman un programa. Incluyen desde operadores aritméticos y lógicos básicos (`+`, `-`, `and`, `or`) hasta instrucciones especializadas, como el guardado de archivos o el volcado de texto en pantalla.

### 3. Control de Flujo
Se refiere a la secuencia de acciones de un programa. En ciertos puntos, el programa debe tomar decisiones con base en el valor de una variable o una condición. Estas acciones son gestionadas por instrucciones de control de flujo, como:
- Condicionales: `if-then-else`
- Bucles: `for`, `while`
- Selección: `case`

### 4. Funciones y Objetos
Con la programación estructurada surge el empleo de **funciones**: series de instrucciones que realizan tareas específicas y devuelven un resultado. Pueden ser reutilizadas varias veces dentro de un programa. 

Con la programación orientada a objetos surgen los **objetos**: entidades que combinan estructuras de datos (atributos) e instrucciones (métodos). Este paradigma permite que el programador defina sus propios objetos para organizar mejor el código.

## ¿Cómo Elegir un Lenguaje de Programación?

Según el tipo de software que deseamos construir, podríamos utilizar esta guía de lenguajes de programación y algunos conocimientos requeridos:

- **Servidores o Back-end**: Python, Ruby, PHP, Java o .Net. Conocimientos de bases de datos y administración de sistemas.
- **Clientes o Front-end**: HTML, CSS, Javascript. Posiblemente se necesiten conocimientos de diseño.
- **Aplicaciones Móviles**: Objective C o Java (para Android). HTML / CSS para sitios web móviles. Posibles conocimientos sobre servidores.
- **3D o Videojuegos**: C/C++, OpenGL. Conocimientos de animación y diseño artístico.
- **Alto Rendimiento**: C/C++, Java. Conocimientos en matemáticas y análisis cuantitativo.

Es importante mencionar que los lenguajes de programación son herramientas clave para el desarrollo de software. Una de sus funciones es facilitar la comunicación entre la máquina y el usuario a través del software. Por lo tanto, es esencial conocer los tipos de lenguajes, sus características y las plataformas donde se utilizan, para elegir el lenguaje de programación más adecuado según el trabajo a realizar.


