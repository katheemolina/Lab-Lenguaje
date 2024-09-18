# Laboratorio de Lenguajes

## Clase 3: 27/08/2024

**Temas**: 
- Problemas de las técnicas tradicionales (procedurales)
- Resolucion de problemas complejos
- El problema de la Extensibilidad, el reuso y el mantenimiento
- Evolución de los lenguajes de POO

## Índice de Contenidos


### La Crisis del Software: Introducción

**La Crisis del Software** es un término informático que se popularizó en 1968, durante la primera conferencia organizada por la OTAN sobre desarrollo de software. El término fue popularizado por Friedrich Ludwig Bauer, quien presidió la conferencia y es conocido por proponer el concepto de "pila" en computación. También fue mencionado por Edsger Dijkstra en su obra "The Humble Programmer".

El término refleja las dificultades del desarrollo de software en comparación con el rápido crecimiento de la demanda de sistemas informáticos, la complejidad de los problemas a resolver y la falta de técnicas establecidas para el desarrollo de software que funcionaran adecuadamente o pudieran ser validadas.

Durante finales de los años 50 y principios de los 60, la potencia computacional de las máquinas era limitada. Los programas desarrollados eran "simples" y seguían un proceso de desarrollo artesanal, sin una metodología establecida. Los lenguajes de bajo nivel eran comunes en esta época.

A finales de los 60, la potencia de las máquinas aumentó considerablemente, y surgieron los lenguajes de programación de alto nivel. Las máquinas requerían programas más complejos que los desarrollados anteriormente, pero este avance en hardware no fue acompañado por una evolución en el desarrollo de software.

Se empezó a concebir el software como un producto, pero surgieron problemas significativos: los productos excedían los costos estimados, había retrasos en las entregas, las prestaciones no cumplían con las expectativas, el mantenimiento era complicado e incluso imposible, y las modificaciones resultaban extremadamente costosas.

En resumen, se producía software de baja calidad porque las técnicas utilizadas para desarrollar programas simples ya no eran adecuadas para la complejidad creciente de los sistemas.

Como ejemplo, observen este gráfico del año 1979, en el que se recoge la inversión en desarrollo de sistemas software, y cómo terminó ese software.

![image](https://github.com/user-attachments/assets/e5ee525f-d4be-457b-b493-05c0d44b5466)

### Causas

Una de las principales causas de la crisis del software era el enfoque inadecuado del proceso de desarrollo, que era deficiente o incluso inexistente. Solo se dedicaba una cuarta parte del tiempo a las fases de análisis, diseño, codificación y pruebas, mientras que más de tres cuartas partes del tiempo se destinaban a correcciones y mantenimiento. Esta falta de inversión en las fases iniciales provocaba errores graves que dificultaban la implementación, resultando en paradas y retrocesos constantes.

El conjunto de las fases de análisis y diseño solo abarcaba el 8% del tiempo total de desarrollo, y casi el 80% de los errores se producían en estas fases, lo que aumentaba el costo de corrección de errores a medida que avanzaban las fases. Con estos indicadores, estaba claro que el proceso de desarrollo de software necesitaba un cambio radical.

### La Solución

Para solucionar "la crisis del software", se estableció la **Ingeniería del Software**. Según Pressman, la Ingeniería del Software es "una disciplina que integra métodos, herramientas y procedimientos para el desarrollo de software de computador". En otras palabras, es una disciplina que busca racionalizar el proceso de desarrollo de software y establecer pautas para minimizar el tiempo, el esfuerzo y los costos de desarrollo, mientras maximiza la calidad del software.

Después de la crisis, se intentaron establecer pautas para mejorar el desarrollo de software, aplicándolas a algunos proyectos y aumentando la inversión. En 1991, se realizó un estudio que mostró resultados positivos: el 52% de los proyectos se terminaron con éxito, frente al 2% en 1979; el 31% se terminó con algunas modificaciones respecto a lo acordado inicialmente, frente al 3% en 1979.

El resultado más notable fue la reducción de proyectos abandonados. En 1991, solo se abandonó el 16,2% de los proyectos, frente al casi 76% en 1979, lo que demuestra la eficacia de los métodos aplicados.

La **Ingeniería del Software** nació como una nueva disciplina que busca software de calidad, que cumple con los requisitos funcionales y de rendimiento establecidos previamente, y cuenta con estándares de desarrollo bien documentados. Además, se enfoca en la calidad del software durante todo el proceso de desarrollo, incorporando nuevos modelos de desarrollo y paradigmas de programación que hacen que el desarrollo sea más metodológico y estructurado.

Una imagen que grafica la problemática del desarrollo de software:

![image](https://github.com/user-attachments/assets/5cb6af3c-c5fc-40ef-9658-870575ad418a)

# Problemas Complejos en el Desarrollo de Software

## Introducción

Los sistemas de software actuales suelen resolver problemas complejos que requieren soluciones confiables, eficientes y capaces de adaptarse dinámicamente a los cambios en las necesidades de los usuarios. El desarrollo de un sistema de software con estas características sigue un ciclo de vida conformado por etapas que pueden organizarse de diferentes formas.

### Proceso de Desarrollo de Software

El desarrollo de software se realiza dentro del marco de un proyecto que establece un cronograma y un presupuesto. El éxito del proyecto está ligado a la calidad del producto final, el sistema de software, pero también es fundamental completar el proyecto con los recursos previstos en el presupuesto y los tiempos establecidos en el cronograma.

Aunque el desarrollo de software es una actividad creativa, requiere la aplicación de un paradigma que guíe, oriente y sistematice cada etapa.

### Paradigma de Programación

Un paradigma de programación brinda:

- **Principio**: Describe propiedades generales que se aplican a todo el proceso de desarrollo.
- **Metodología**: Consta de un conjunto integrado de métodos, estrategias y técnicas que aseguran la aplicación del principio.
- **Herramientas**: Conjunto de herramientas que soportan y facilitan la aplicación de la metodología.

### Clasificación de Sistemas de Software

Los sistemas de software se pueden clasificar de acuerdo a diferentes criterios, generalmente en tres categorías: sistemas de pequeña, mediana y gran complejidad. Aunque no hay límites precisos que separen estas categorías, el tiempo y el costo de desarrollo son los principales factores que determinan la escala de un sistema.

### Calidad del Software

La calidad de un producto de software puede definirse como su capacidad para satisfacer las necesidades del usuario establecidas durante el desarrollo de requerimientos. La calidad puede evaluarse de acuerdo a distintos factores, algunos de los cuales son percibidos por el usuario o cliente, mientras que otros afectan indirectamente.

### Productividad del Software

La productividad implica reducir tiempos y costos en la concepción y construcción de un sistema, y está fuertemente ligada a dos cualidades fundamentales: **extensibilidad** y **reusabilidad**.

- **Extensibilidad**: Un producto de software es extensible si es fácil adaptarlo a cambios en la especificación.
- **Reusabilidad**: Un módulo de software es reusable si puede utilizarse para la construcción de diferentes aplicaciones.

La extensibilidad afecta fundamentalmente al mantenimiento, pero depende de las etapas anteriores del desarrollo.

La capacidad de mantenimiento se centra en las modificaciones relacionadas con correcciones de errores y modificaciones de funciones menores, y no en extensiones funcionales importantes. El mantenimiento puede ser soportado con una definición de interfaz útil, documentación y documentación de código o código autodocumentado. Cuanto más adecuada y útil sea la documentación, más fácil será realizar el mantenimiento.

## Evolución de los Lenguajes de Programación Orientada a Objetos (POO)

La Programación Orientada a Objetos (POO) define una serie de conceptos y técnicas para representar acciones o cosas de la vida real mediante objetos. A diferencia de la programación estructurada, la POO trabaja con conceptos como clases, objetos, métodos, propiedades, estados, herencia, y encapsulación, generando interrelaciones en el desarrollo para el funcionamiento del sistema principal. 

### Pilares de la Programación Orientada a Objetos

Los pilares fundamentales de la POO son:
- **Herencia**
- **Encapsulamiento**
- **Polimorfismo**
- **Abstracción**

### Simula 67

El primer lenguaje orientado a objetos fue **Simula 67**, desarrollado por Krinsten Nygaard y Ole-Johan Dahl en 1967. Introdujo las nociones de clase y herencia jerárquica, pero no admite la herencia múltiple. El ocultamiento de la información se realiza protegiendo características para evitar su herencia en el futuro. Permite la sobrecarga de métodos y la comprobación de tipos puede ser estática o dinámica.

### Smalltalk

Desarrollado en el Centro de Investigación Palo Alto Xerox a principios de los años 70, **Smalltalk** fue el primer lenguaje puramente orientado a objetos, utilizando exclusivamente clases y objetos. Las características comunes de los objetos Smalltalk incluyen:
- Memoria propia
- Capacidad de comunicación con otros objetos
- Herencia de características de objetos ancestros
- Capacidad de procesamiento

Smalltalk encapsula variables globales dentro de módulos, permitiendo el acceso solo a través de operaciones definidas, creando una interfaz.

### C++

Creado por Bjarne Stroustrup en 1983, **C++** extiende el lenguaje C con características orientadas a objetos. Introduce nuevos mecanismos para la manipulación de objetos y es considerado un lenguaje híbrido, apoyando programación estructurada y orientada a objetos, además de la programación genérica. C++ agrega palabras clave y operadores específicos para el manejo de clases y tiene tipos fundamentales como char, int, float, y bool.

### Eiffel

**Eiffel** es un lenguaje orientado a objetos diseñado por Bertrand Meyer en 1985. Destaca por su diseño por contrato, que facilita la detección de errores y la depuración. Las clases son la unidad básica y la gestión de memoria es automática a través del recolector de basura. Soporta herencia múltiple, aunque tiene desventajas en el manejo de memoria y librerías de clases reducidas. Los compiladores para Eiffel incluyen Small Eiffel, ISE Eiffel y Visual Eiffel.

### Delphi

**Delphi** no es únicamente un lenguaje orientado a objetos, sino un entorno de desarrollo para programación visual. La versión Object Pascal, desarrollada por Apple Computer en 1986, se especializa en programación orientada a objetos. Borland Delphi, lanzado en 1995, presentó una nueva sintaxis utilizando "class" en lugar de "object", el constructor "Create" y un destructor virtual "Destroy", manteniendo compatibilidad con la sintaxis anterior.

### JAVA

**JAVA**, creado en 1995, es un lenguaje orientado a objetos que se popularizó rápidamente. Todos los tipos, excepto los fundamentales (int, char, long), son clases. JAVA es independiente de la arquitectura, permitiendo su ejecución en diferentes sistemas operativos. Proporciona una colección de clases para aplicaciones de red y se basa en principios de programación orientada a objetos como herencia y polimorfismo. Su sintaxis deriva de C++ pero está diseñado completamente para ser orientado a objetos.

### C#

Desarrollado por Microsoft en los años 2000, **C#** es un lenguaje orientado a objetos que incorpora características de C, C++ y JAVA. Utiliza plantillas de proyecto, diseñadores y asistentes de código. C# es simple, eficaz, y seguro en tipos. Las variables de objeto almacenan referencias en lugar de valores y el operador de asignación copia referencias en lugar de valores. Permite desarrollar componentes de software para ambientes distribuidos y su código fuente es portable.


