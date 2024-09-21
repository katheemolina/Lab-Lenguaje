# Laboratorio de Lenguajes

## Clase 2: 21/08/2024

### Temas:
- Perspectiva histórica de los lenguajes de programación: 
  - Motivación
  - Herencia
  - Características
  - Evolución

## Índice de Contenidos
- [FORTRAN](#fortran)
- [COBOL](#cobol)
- [BASIC](#basic)
- [LOGO](#logo)
- [C](#c)
- [PASCAL](#pascal)
- [PROLOG](#prolog)
- [ADA](#ada)
- [JAVA](#java)
- [PYTHON](#python)
- [Otros lenguajes](#otros-lenguajes)
  - [PLANKALKÜL](#plankalkül)
  - [SHORT CODE](#short-code)
  - [FLOWMATIC](#flowmatic)
  - [LISP](#lisp)
  - [ALGOL (continuación)](#algol-continuación)
  - [JOVIAL](#jovial)
  - [APL](#apl)

---

### **FORTRAN**

Al comienzo de la década de los 50, **John Backus** estaba trabajando con SSEC (Selective Sequence Electronic Calculator), una de las primeras computadoras de IBM, y desarrolló el programa **SPEEDCODING** para ese modelo. A partir de esa experiencia, en otoño de 1954, comenzó la creación de un lenguaje que agregaría más prestaciones al modelo **IBM 704**, que iba a salir pronto al mercado.

En 1956 se terminó el compilador **FORTRAN** (FORmula TRANslator), que se incluyó en el IBM 704, junto con un manual de 51 páginas.

Como su nombre indica, FORTRAN estaba (y está) destinado a la resolución de problemas científico-técnicos, resultando relativamente sencillo de aprender si se domina la notación matemática. Aunque ha ido perfeccionándose a lo largo del tiempo (con sus versiones II, IV, 77 y 90), lo cierto es que se ha visto superado por otros lenguajes debido a la falta de estructuración de sus programas, lo que los hace difíciles de seguir.

Sin embargo, FORTRAN todavía se utiliza, sobre todo en el ámbito universitario, debido a la gran biblioteca de subrutinas y funciones que se ha ido creando en más de treinta años de existencia.

---

### **COBOL**

A finales de los 50, el Departamento de Defensa de los Estados Unidos estaba preocupado con los lenguajes de programación existentes, principalmente por dos razones: 
1. Los programas no podían trasladarse de una computadora a otra.
2. Los programas eran difíciles de leer y modificar.

Para resolver estos problemas, se patrocinó una conferencia sobre lenguajes (CODASYL: **COnference on DAta SYstems Languages**), que tuvo lugar en 1959 y en la que participaron las grandes empresas del sector (IBM, Sperry Rand, Honeywell, etc.).

Como resultado de esa conferencia, surgieron las especificaciones para desarrollar **COBOL** (COmmon Business Oriented Language), un lenguaje orientado a funciones administrativas, con gran portabilidad y legibilidad. Su primera versión apareció al año siguiente, y posteriormente surgieron nuevas actualizaciones como COBOL 74 y COBOL 85.

Dado que COBOL buscaba ser fácil de leer, tiene una sintaxis muy similar al inglés común, con una terminología que incluye verbos, párrafos, frases, entre otros. Los programas se estructuran en cuatro divisiones:
1. **Identification**
2. **Environment**
3. **Data**
4. **Procedure**

Cada división se subdivide en secciones, que a su vez contienen párrafos, frases e instrucciones.

Actualmente, **COBOL** se utiliza casi exclusivamente en algunos grandes sistemas informáticos, principalmente en entidades bancarias, aunque su uso se limita mayormente al mantenimiento del código existente en lugar de desarrollar nuevas aplicaciones.

---
### **BASIC**

**John G. Kemeny** y **Thomas E. Kurtz**, profesores del Dartmouth College (New Hampshire), diseñaron en 1964 un nuevo lenguaje para introducir a sus estudiantes en los sistemas de tiempo compartido. Este lenguaje, llamado **BASIC** (Beginner's All-purpose Symbolic Instruction Code), se ha convertido en uno de los lenguajes más difundidos, aplicándose tanto en tareas de gestión como en aplicaciones científicas.

**¿Por qué es tan popular BASIC?**

Aunque no era el mejor ni el más potente lenguaje, tenía dos grandes ventajas:
1. Era sencillo de aprender.
2. Su intérprete ocupaba poca memoria.

Cuando se creó la primera computadora personal (Altair de MITS), se desarrolló una versión de BASIC para ella, diseñada por **Microsoft**. Más tarde, Microsoft adaptó su BASIC a productos de **Apple**, a microordenadores, y lo más importante, al **PC de IBM**, incluyendo la versión **GW-BASIC** en su sistema operativo MS-DOS.

Muchos aprendieron a programar en BASIC con sus ZX-Spectrum o su primer PC. Una vez dominado un lenguaje, es comprensible una cierta reticencia al cambio.

Además de GW-BASIC, hubo otras versiones con cierta difusión en los 80, como **Turbo BASIC** (de Borland) y **QuickBASIC** (de Microsoft). Incluso Kemeny y Kurtz intentaron aprovechar el éxito de su creación con **True BASIC** en 1983, aunque su comercialización no fue muy fructífera. 

BASIC ha sabido adaptarse a las necesidades del mercado. Las primeras versiones eran interpretadas y sus programas resultaban un tanto ilegibles; en cambio, las versiones actuales incorporan bastante estructuración y son compiladas. El exponente máximo de los modernos BASIC es **Visual BASIC** de Microsoft.

---
### **LOGO**

En 1964, **Seymour Papert** se incorporó al MIT tras haber colaborado con el pedagogo **Jean Piaget** en Suiza. Tres años después, Papert comenzó a diseñar un lenguaje para introducir a los estudiantes más jóvenes en el mundo de la programación, con el lema: «¡Que los niños programen a los ordenadores y no los ordenadores a los niños!».

Poco a poco, **LOGO** fue perfeccionándose y, en 1980, Papert lo divulgó mundialmente con su libro *Mindstorms: Children, Computers, and Powerful Ideas*. LOGO fue muy bien recibido en los ámbitos educativos, especialmente en enseñanza primaria y secundaria.

Teniendo en cuenta los pocos conocimientos matemáticos de sus usuarios potenciales, LOGO introduce la programación de manera gráfica, mediante la geometría de la tortuga. Inicialmente, LOGO controlaba un pequeño robot con ruedas, motor y un lápiz retráctil, que admitía órdenes sencillas e intuitivas (Avanzar, Retroceder, Girar a la derecha, etc.) y trazaba dibujos en el papel. La tortuga recibió su nombre por su forma abombada y por ser bastante lenta.

A pesar del impulso inicial prometedor, LOGO ha ido desapareciendo de los centros de enseñanza españoles. Las causas incluyen la complejidad del lenguaje cuando se intenta ir más allá de la tortuga gráfica, con el uso continuo de listas y procedimientos recursivos, y el cambio en la informática educativa hacia una informática de usuario, centrada en el manejo de aplicaciones ofimáticas.

---
### **C**

En los Laboratorios Bell (New Jersey), **Kenneth Thompson** y **Dennis Ritchie**, creadores del sistema operativo UNIX, desarrollaron en 1969 un lenguaje experimental llamado **B**. Dos años después, Ritchie creó un nuevo lenguaje basado en B, llamado **C**. C es uno de los lenguajes más portables del mercado y ofrece amplias prestaciones.

A principios de los 80, **Bjarne Stroustrup** diseñó una ampliación de C y, en 1984, la convirtió en un compilador llamado **C++**, especialmente enfocado en la programación orientada a objetos.

---
### **PASCAL**

A principios de los 70, el profesor suizo **Niklaus Wirth**, del Instituto Politécnico Federal de Zurich, emprendió la creación de un nuevo lenguaje, **PASCAL**, que permitiera introducirse en la programación de una forma fácil pero a la vez potente y siguiendo unas pautas estructuradas. De hecho, PASCAL es el lenguaje más sencillo que posibilita el acceso a la informática teórica: descomposición modular, recursividad, punteros, etc.

PASCAL, que surgió como una derivación de ALGOL, fue definido en el libro *PASCAL - User Manual and Report* (1974), escrito por Kathleen Jensen y Niklaus Wirth. En 1980 sufrió la primera formalización y se estandarizó en 1983. Al poco tiempo, **Borland** lanzó al mercado su compilador PASCAL, llamado **Turbo Pascal**, para recalcar su rapidez. Su éxito fue tan grande que vendió casi medio millón de copias de su compilador sólo en 1985.

Durante más de una década, Turbo Pascal ha sido sinónimo de PASCAL, pero en el año 2000, Borland dejó de darle soporte técnico y su presencia es cada día menor en el ámbito de la programación, sobreviviendo a duras penas en el mundo universitario. Sin embargo, en 1995 surgió una nueva versión, **DELPHI**, que amplía PASCAL a la programación visual e intenta hacerle la competencia a Visual BASIC.

---
### **PROLOG**

En 1972, **Robert Kowalski** (Universidad de Edimburgo) y **Alain Colmerauer** y **Philippe Roussell** (Universidad de Aix-Marseille) expusieron la revolucionaria idea de que la lógica podía emplearse como lenguaje de programación. Siguiendo esta línea, al año siguiente, el grupo de inteligencia artificial de la Universidad de Aix-Marseille comenzó a diseñar ese lenguaje, al que se llamó **PROLOG** (PROgramation LOGique).

Es el prototipo de lenguaje declarativo por excelencia. ¿Qué significa declarativo? Todos los lenguajes que hemos visto hasta ahora son algorítmicos; es decir, debemos indicar todos y cada uno de los pasos a seguir para realizar una cierta tarea. Frente a estos lenguajes imperativos, los declarativos no están basados en órdenes sino en descripciones. En otras palabras, en PROLOG se proporciona a la computadora una serie de conocimientos sobre un tema, junto con una serie de reglas, y el programa nos contestará todas aquellas preguntas que deseemos hacerle sobre el tema, siempre que las respuestas puedan deducirse lógicamente de los conocimientos dados al inicio.

Como es fácil suponer, PROLOG no está destinado al cálculo científico. Su aplicación en el campo de la inteligencia artificial, definiendo objetos y estableciendo relaciones, permite resolver problemas lógicos, desarrollar sistemas expertos, investigar en la comprensión del lenguaje humano, etc.

---
### **ADA**

Quince años después de intentar uniformizar los lenguajes con COBOL, el **Departamento de Defensa de EE.UU.** percibió que su objetivo no se había cumplido. Por ese motivo, en 1975 formó un grupo de trabajo para evaluar los lenguajes existentes en aquel entonces y ver si alguno de ellos podía adaptarse a las necesidades del Departamento.

**¿Qué objetivos debía cumplir el lenguaje deseado?**
1. Debía permitir el diseño de programas modulares y estructurados, de modo que fueran fáciles de leer y depurar.
2. Tenía que gestionar cualquier periférico para controlar instrumentos militares.
3. Debía aceptar el trabajo en paralelo, permitiendo que varios procesos se ejecutaran simultáneamente.

El grupo de trabajo no encontró un lenguaje adecuado y propuso la creación de un nuevo lenguaje basado en **PASCAL**, **PL/I** y **ALGOL 68**, ya que eran los más apropiados de los evaluados. Se convocó un concurso para desarrollar un nuevo lenguaje que se ajustara a los requerimientos del Departamento de Defensa. Se presentaron 17 propuestas y quedaron reducidas a cuatro, con los nombres clave **Red**, **Green**, **Yellow** y **Blue**, para preservar el anonimato.

Finalmente, **Green** fue el lenguaje elegido. Propuesto por **Honeywell-Bull** (Francia), fue diseñado por un equipo encabezado por **Jean Ichbiah**. En un primer momento, se le dio el nombre de **DoD-1**, pero se cambió a **ADA**, en honor a Ada Lovelace.

A pesar de los años transcurridos y las mejoras introducidas en él, ADA no es un lenguaje popular, salvo por su nombre. Se le reprocha ser un tanto complejo, bastante estricto y sólo apropiado para el desarrollo de grandes programas.

---
### **JAVA**

Este lenguaje, hoy en día ampliamente utilizado en Internet, fue desarrollado en 1990 por **James Gosling**, de **Sun Microsystems**, basándose en **C** y **C++**. En una época en la que la Red estaba casi circunscrita al ámbito universitario, el objetivo de Sun no era específicamente para Internet, sino crear una interfaz atractiva e intuitiva para electrónica de consumo (calculadoras, televisión interactiva, etc.).

Sin embargo, la electrónica de consumo no evolucionó como se esperaba y, durante unos años, el lenguaje de Gosling permaneció aparcado. Más tarde, **Bill Joy** (cofundador de Sun) consideró que el lenguaje podría ser interesante para Internet y propuso modificarlo para el nuevo medio. En agosto de 1995, ya con el nombre de **JAVA**, se presentó en sociedad.

A pesar de que JAVA resulta un tanto lento en su ejecución, cada día es más popular. Por un lado, es relativamente sencillo y bastante potente; además, es válido para cualquier plataforma y, sobre todo, muy fiable y seguro.

---
### **PYTHON**

La historia de **Python** como lenguaje de programación inicia a finales de los 80 y principios de los 90 con **Guido Van Rossum**, una historia de 29 años de desarrollo. En una Navidad de 1989, Guido Van Rossum, quien trabajaba en el **CWI** (un centro de investigación holandés), decidió empezar un proyecto como pasatiempo dándole continuidad a **ABC**, un lenguaje de programación desarrollado en el CWI.

**ABC** fue desarrollado a principios de los 80 como alternativa a **BASIC**, pensado para principiantes por su facilidad de aprendizaje y uso. Su código era compacto pero legible. El proyecto no trascendió debido a que el hardware disponible en la época dificultaba su uso. Así que Van Rossum le dio una segunda vida creando Python. A Guido Van Rossum le gustaba mucho el grupo **Monty Python**, por esta razón escogió el nombre del lenguaje. Actualmente, Van Rossum sigue ejerciendo un rol central en la dirección de Python.

En 1991, Van Rossum publicó el código de la versión 0.9.0. En esta versión ya estaban disponibles clases con herencias, manejo de excepciones, funciones y los tipos modulares. Esta versión introdujo un sistema de módulos adoptado de **Modula-3**, un lenguaje de programación estructurado y modular, el cual Guido describe como una de las mayores unidades de programación de Python. Por ejemplo, el modelo de excepciones de Python es parecido al de Modula-3.

Para 1994 se creó **comp.lang.python**, un foro de discusión de Python que marcó un hito en su popularidad y multiplicó su cantidad de usuarios.

Uno de los proyectos más impresionantes escritos en Python es el **servidor de Dropbox**, donde actualmente trabaja Guido, que hoy en día sirve a millones de personas. Otro uso notable es en la comunidad científica como herramienta para **Machine Learning**.

---
### **Otros lenguajes**

Además de los lenguajes vistos anteriormente, se han ido desarrollando muchos otros, aunque sus ámbitos de aplicación sean más reducidos o ya han dejado de utilizarse. A continuación, veremos algunos que han tenido cierto interés y/o influencia.

### PLANKALKÜL

Podríamos decir que es el antepasado de los modernos lenguajes de programación. Fue creado por **Konrad Zuse**, a mediados de los 40, para su serie de máquinas Z. Su nombre es una combinación de las palabras Plan y Kalkül, así que podría traducirse por «plan de cálculo».

### SHORT CODE

Basándose en las ideas de **John W. Mauchly**, **William F. Schmitt** creó este lenguaje interpretado en 1950 y fue utilizado en la primera serie de **UNIVAC**. Es considerado el precursor de los lenguajes de alto nivel.

### FLOWMATIC

El primer lenguaje de programación destinado al tratamiento de aplicaciones de gestión. Desarrollado por el equipo de **Grace Hopper** en 1957, este lenguaje compilado sólo fue implementado en **UNIVAC**.

### LISP

Durante un encuentro sobre inteligencia artificial celebrado en el verano de 1956, **H. A. Simon**, **A. Newell** y **J. C. Shaw** describieron su lenguaje **IPL (Information Processing Language)**, creado para la computadora **JOHNIAC**. Inspirándose en ese lenguaje, en 1958 **John McCarthy** creó **LISP (LISt Processing language)** como parte de un proyecto de inteligencia artificial del MIT, teniendo como soporte un equipo **IBM 704**. Se trata de un lenguaje conciso e interactivo, basado en el tratamiento de listas (de ahí su nombre), ya que, tanto los programas como los datos se estructuran mediante listas.

### ALGOL (continuación)

Con vistas a obtener un lenguaje universal, que no dependiera de la máquina donde se implementara, se formó un comité internacional, formado por la **ACM (Association for Computing Machinery)** y la **GAMM** (siglas alemanas de la Sociedad para las Matemáticas aplicadas), que, en 1958, publicó en Zurich un informe dando carta de nacimiento al **IAL (International Algebraic Language)**, posteriormente denominado **ALGOL 58 (ALGOritmic Language)**. Su versión operativa se presentó en París en 1960 y, más adelante, fue perfeccionada (ALGOL 68).

Aunque ha caído en desuso, su influencia ha sido decisiva en el desarrollo de los lenguajes de programación posteriores, ya que muchos de los más importantes (**PASCAL**, **C**, **ADA**, **JAVA**, etc.) descienden, directa o indirectamente, de **ALGOL**.

### JOVIAL

Su nombre son las siglas de **«Jules’ Own Version of the International Algorithmic Language»** y fue desarrollado en 1959, partiendo de IAL (de ahí el nombre), para **Air Force USA**, que deseaba un lenguaje válido tanto para usos científicos como de gestión. **JOVIAL** todavía sigue activo.

### APL

El profesor **Kenneth E. Iverson** ideó una notación para describir, sin ambigüedad y con concisión, algoritmos matemáticos y la dio a conocer en su libro **«A Programming Language»** (cuyas siglas corresponden al nombre del lenguaje), publicado en 1962. Partiendo de esa notación, **IBM** desarrolló el lenguaje **APL**, orientado a usos científicos. Todavía se sigue utilizando y sus programas se reconocen visualmente por su brevedad y la inclusión de caracteres especiales.

### PL/I

Este lenguaje fue desarrollado por **IBM**, a partir de 1963, que deseaba un lenguaje polivalente, en el sentido de que podía aplicarse tanto a gestión como al ámbito científico. Buscando aunar las ventajas de **COBOL**, **FORTRAN** y **ALGOL**, **PL/I** resultó un lenguaje muy flexible y potente, por lo que todavía sigue en uso.

### RPG

A principios de los 60, **IBM** comenzó a desarrollar un lenguaje orientado a la obtención de informes (ventas, pagos, etc.) en el ámbito de gestión (**RPG** son las siglas de **Report Program Generator**).

En 1964 salió al mercado con la serie **IBM 360** y, desde entonces, ha sufrido diversas actualizaciones: II, III, 400, IV, **Visual RPG**. Es un lenguaje sencillo de aprender, si bien su versatilidad no es mucha. En las cuatro secciones en que se estructura cada programa, se deben indicar los archivos y dispositivos a emplear, fijar las especificaciones de entrada, determinar las operaciones a realizar y establecer los formatos de salida. A partir de la versión IV se añadió la sección de subprocedimientos.

### SIMULA

Basado en **ALGOL**, se trata del primer lenguaje orientado a objetos. Fue desarrollado por los noruegos **Ole-Johan Dahl** y **Kristen Nygaard** que buscaban un lenguaje adecuado para la simulación de eventos discretos (su nombre es una contracción de **Simulation Language**). Su primer compilador estuvo disponible en 1964, para la serie 1100 de **UNIVAC**, si bien hasta 1967 no adquirió una amplia funcionalidad. En la actualidad hay disponibles diversas versiones freeware de su compilador.

### FORTH

Este lenguaje fue creado a finales de los 60 por **Charles H. Moore**, para controlar los radiotelescopios de Kitt Peak y procesar sus datos. Se trata de un lenguaje funcional e interactivo que ha ido evolucionando con el paso del tiempo. Debido a la poca memoria que ocupa y a su rapidez, fue uno de los primeros en difundirse entre los microordenadores.

### LSE

Con objeto de que el profesorado francés de secundaria fuese capaz de crear sus propios materiales educativos informáticos, se diseñó el lenguaje **LSE (Langage Symbolique d’Enseignement)** en 1971, que no tuvo mucho éxito.

### SMALLTALK

Creado por **Alan Kay** en el **Centro de Investigaciones Xerox** de Palo Alto, en los primeros 70, es un lenguaje muy influenciado por **SIMULA**, estando también orientado a objetos. Tuvo sucesivas versiones (72, 76 y 80) y ofrece un entorno completo para el desarrollo de software.

### COMAL

Destinado a la informática educativa en los países escandinavos, fue desarrollado por **Benedict Loefstedt** y **Borge Christensen** en 1973, combinando las ventajas de **BASIC** y **PASCAL** (sus siglas corresponden a **COMmon Algorithmic Language**). En 1980 se estandarizó y todavía sigue siendo utilizado, sobre todo en la Europa del norte.
