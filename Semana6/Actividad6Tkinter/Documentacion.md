
# Proyecto: Sistema de Gestión de Jugadores de Fútbol

## Descripción General

Este proyecto tiene como objetivo desarrollar un sistema orientado a objetos para que un Director Técnico pueda gestionar y consultar las estadísticas de los jugadores de su equipo de fútbol. El sistema se enfoca en la creación, almacenamiento y consulta de datos de los jugadores, permitiendo controlar sus estadísticas de manera eficiente mediante una **Interfaz Gráfica de Usuario (GUI)** construida con `Tkinter`.

El sistema se organiza en clases utilizando **herencia** para representar los distintos tipos de jugadores, diferenciando sus características comunes (como número de camiseta, apellido y minutos jugados) y específicas (como la cantidad de goles para jugadores que no son arqueros). 

## Situación Problemática

El Director Técnico necesita un sistema para llevar el control de los siguientes datos de los jugadores:
- **Número de camiseta**: Identificador único de cada jugador.
- **Apellido**: Apellido del jugador.
- **Posición**: Cada jugador ocupa una de las siguientes posiciones: arquero, defensor, central o delantero.
- **Minutos jugados**: Tiempo en minutos que ha jugado cada jugador.
- **Cantidad de goles**: Número de goles marcados (solo para defensores, centrales y delanteros).

El objetivo del sistema es permitir:
- **Cargar jugadores** al sistema con sus respectivos datos.
- **Consultar las estadísticas** de todos los jugadores ingresados.
- **Agregar goles** a aquellos jugadores que tienen la capacidad de marcarlos (defensores, centrales y delanteros).

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

```
.
|-- __pycache__
|-- gui/
|   |-- __init__.py
|   |-- interfaz.py
|-- jugadores/
|   |-- __init__.py
|   |-- arquero.py
|   |-- central.py
|   |-- defensor.py
|   |-- delantero.py
|   |-- jugador.py
|   |-- jugador_con_goles.py
|-- main.py
```

### Clases y Herencia

Se utilizan varias clases para representar los diferentes tipos de jugadores, siguiendo un modelo orientado a objetos. Las clases clave incluyen:

- **Jugador (jugador.py)**: Clase base que representa a cualquier jugador, con atributos como el número de camiseta, apellido, posición y minutos jugados.
- **JugadorConGoles (jugador_con_goles.py)**: Hereda de la clase `Jugador` y agrega la funcionalidad de almacenar y contar goles. Es utilizada por jugadores que no son arqueros.
- **Arquero (arquero.py)**: Hereda de `Jugador` y representa a los arqueros, quienes no tienen la capacidad de marcar goles.
- **Defensor, Central, Delantero**: Heredan de `JugadorConGoles` y permiten registrar goles, además de los atributos comunes de un jugador.

### Interfaz Gráfica de Usuario (GUI)

El sistema incluye una interfaz gráfica de usuario, implementada en [tkinter](https://docs.python.org/es/3/library/tkinter.html), que permite interactuar de forma sencilla con las funcionalidades del sistema. 

#### Funcionalidades Principales:
1. **Cargar Jugador**: Permite ingresar un nuevo jugador con su número de camiseta, apellido, posición y minutos jugados. Dependiendo de la posición, se instancia la clase correspondiente (por ejemplo, `Arquero`, `Delantero`).
   
2. **Consultar Estadísticas**: Muestra un listado con las estadísticas de todos los jugadores registrados, incluyendo la cantidad de goles para aquellos jugadores que puedan marcarlos.

3. **Agregar Goles**: Permite seleccionar un jugador que no sea arquero y añadirle goles.

4. **Salir del Sistema**: Opción para cerrar la aplicación.

El archivo `interfaz.py` contiene todas las funcionalidades que permiten interactuar con el sistema, mediante botones que ejecutan las acciones como cargar jugadores, consultar estadísticas y agregar goles.

### Relación entre Clases

La relación de herencia entre las clases permite que las posiciones de los jugadores se gestionen de manera eficiente. La clase base `Jugador` maneja atributos comunes a todos los jugadores, mientras que `JugadorConGoles` extiende esta funcionalidad para jugadores que pueden marcar goles. Las subclases `Arquero`, `Defensor`, `Central` y `Delantero` se encargan de representar posiciones específicas.

## Descripcion de archivos

- **main.py**: Archivo principal que lanza la interfaz gráfica y establece el menú principal con las opciones disponibles.
- **interfaz.py**: Controla la interacción con la GUI y contiene las funciones que permiten cargar jugadores, consultar estadísticas y agregar goles.
- **jugador.py**: Clase base que define los atributos comunes de los jugadores.
- **jugador_con_goles.py**: Extiende la funcionalidad de `Jugador` para aquellos que pueden marcar goles.
- **arquero.py**, **defensor.py**, **central.py**, **delantero.py**: Subclases específicas que implementan jugadores en distintas posiciones.

# Glosario de funcionalidades y métodos utilizados

## Python

### `__init__`:
Método especial en Python que actúa como constructor en una clase. Es invocado cuando se crea una instancia de la clase, permitiendo inicializar los atributos del objeto. 

Como por ejemplo, `__init__` se usa para inicializar los atributos de cada jugador cuando se crea un objeto de la clase Jugador.

```python
class Jugador:
    def __init__(self, numero_camisa, apellido, posicion, minutos_jugados=0):
        self.numero_camisa = numero_camisa
        self.apellido = apellido
        self.posicion = posicion
        self.minutos_jugados = minutos_jugados
```
### `super()`:
Función que llama al método de una clase padre. Se utiliza para acceder a métodos y propiedades de una clase base desde una subclase.

Se utiliza `super()` para llamar al constructor de la clase padre (Jugador) y reutilizar su lógica de inicialización.

```python
class Arquero(Jugador):
    def __init__(self, numero_camisa, apellido, minutos):
        super().__init__(numero_camisa, apellido, "Arquero", minutos_jugados=minutos)
```


### `match case`:
Estructura condicional introducida en Python 3.10 que permite comparar un valor contra patrones (similar al `switch` en otros lenguajes). Es usada para realizar operaciones basadas en diferentes opciones.

Este bloque utiliza match case para verificar la posición del jugador y ejecutar una acción según el rol.
```python
    match posicion:
        case "arquero":
            jugador = Arquero(numero, apellido, minutos)
        case "defensor":
            jugador = Defensor(numero, apellido, minutos)
        case "central":
            jugador = Central(numero, apellido, minutos)
        case "delantero":
            jugador = Delantero(numero, apellido, minutos)
        case _:
            messagebox.showerror("Error", "Posición no válida. El jugador no se cargó.")
```

### `isdigit()`:
Método que verifica si todos los caracteres de una cadena son dígitos. Retorna `True` si la cadena contiene solo números, `False` de lo contrario.

Se utiliza isdigit() para asegurarse de que el número de camiseta ingresado sea un valor numérico.

```python
if not numero.isdigit():
        messagebox.showerror("Error", "Asegúrese de ingresar un número de camiseta válido.")
        return
```

### `append()`:
Método usado para añadir un elemento al final de una lista. En este caso, se utiliza para agregar jugadores a la lista `jugadores`.

```python
jugadores.append(jugador)
```
---

## Tkinter

### `tk.Tk()`:
Crea una nueva ventana principal en una aplicación de tkinter. Es el contenedor principal para toda la interfaz gráfica.

### `tk.Label()`:
Widget que muestra texto estático en la interfaz. En este caso, se utiliza para mostrar etiquetas descriptivas en el formulario.

### `tk.Entry()`:
Widget que permite al usuario ingresar una sola línea de texto. En tu código, se utiliza para obtener información como el número de camiseta y minutos jugados.

### `ttk.Combobox()`:
Un widget de selección desplegable que permite elegir entre varias opciones. Se utiliza para seleccionar la posición del jugador (Arquero, Defensor, Central, Delantero).

### `tk.Button()`:
Widget que representa un botón interactivo. Se asocia con una función que se ejecuta cuando el usuario lo presiona (como `cargar_jugador` o `consultar_estadisticas`).

### `pack()`:
Método usado para organizar y colocar widgets dentro de la ventana. Distribuye los elementos de manera vertical u horizontal.

### `messagebox.showinfo()`:
Método que abre un cuadro de diálogo informativo. Es utilizado para mostrar mensajes al usuario (por ejemplo, cuando se carga un jugador correctamente).

### `messagebox.showerror()`:
Similar a `showinfo()`, pero muestra un cuadro de diálogo de error cuando ocurre una situación no deseada, como un valor incorrecto en los campos del formulario.

### `delete()`:
Método de los widgets `Entry` que elimina el contenido del campo de texto. Se utiliza para limpiar los campos una vez que se guarda la información.

### `mainloop()`:
Método que inicia el bucle principal de eventos de la interfaz gráfica. Este bucle mantiene la aplicación abierta hasta que el usuario decida cerrarla.

## Ejecuta el codigo

Requisitos previos para la ejecucion de nuestro proyecto:

- **Python:** Asegúrate de tener Python 3.10 o una version posterior instalado (ya que utilizamos un bloque match case en nuestro codigo). Puedes verificarlo ejecutando el siguiente comando en la terminal o en el símbolo del sistema:

   ```bash
   python --version
   ```
- **Tkinter:** generalmente se incluye con la instalación estándar de Python. 


Pasos para Ejecutar la Aplicación
- Clonar el Repositorio 
   ```bash
   git clone https://github.com/katheemolina/Lab-Lenguaje.git
   ```

- Navegar al Directorio del Proyecto
   ```bash
   cd Lab-Lenguaje/Semana6/Actividad6Tkinter
   ```

- Ejecutar el Archivo Principal: 

   ```bash
   python main.py
   ```
- Sigue las instrucciones en la aplicación para gestionar los jugadores.

## Contáctanos

Si tienes preguntas o sugerencias sobre este proyecto, no dudes en ponerte en contacto con nosotros.

Grupo 8:
- [@juanigpunte](https://github.com/Juanigpunte)
- [@agusmoscato](https://github.com/agusmoscato)
- [@katheemolina](https://github.com/katheemolina)
- [@Lorenzoalvarezb](https://github.com/Lorenzoalvarezb)

🌼
