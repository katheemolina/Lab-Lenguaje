## Índice

- [Introducción a Python](#introducción-a-python)
- [PEP 8: Guía de Estilo para Python](#pep-8-guía-de-estilo-para-python)
- [Hola Mundo en Python](#hola-mundo-en-python)
- [Definiendo Variables en Python](#definiendo-variables-en-python)
  - [Constantes](#constantes)
- [Comentarios](#comentarios)
- [Tipos de Datos](#tipos-de-datos)
  - [Tipos Básicos](#tipos-básicos)
  - [Tipos Complejos](#tipos-complejos)
- [Operadores](#operadores)
  - [Operadores Aritméticos](#operadores-aritméticos)
  - [Operadores Comparativos](#operadores-comparativos)
  - [Operadores Lógicos](#operadores-lógicos)


# Introducción a Python

Dentro de los lenguajes de programación, Python puede ser clasificado como un lenguaje interpretado, de alto nivel, multiplataforma, de tipado dinámico y multiparadigma. 

A diferencia de la mayoría de los lenguajes de programación, Python nos provee de reglas de estilo, a fin de poder escribir código fuente más legible y de manera estandarizada. Estas reglas de estilo son definidas a través de la [Python Enhancement Proposal Nº 8 (PEP 8)](https://peps.python.org/pep-0008/#introduction).

## PEP 8: Guía de Estilo para Python

PEP 8 es la guía de estilo para Python que proporciona convenciones para la escritura de código en Python. Algunas recomendaciones importantes son:


- **Nombres de Variables:**
  - Deben ser descriptivos y en minúsculas. Las palabras se separan por guiones bajos (`_`).
  - Ejemplo: `nombre_usuario`, `edad_persona`.


- **Nombres de Constantes:**
  - Deben estar en mayúsculas y las palabras separadas por guiones bajos (`_`).
  - Ejemplo: `MAXIMO_INTENTOS`, `PI`.


- **Nombres de Clases:**
  - Deben usar el estilo CamelCase, donde cada palabra empieza con mayúscula y no se usan guiones bajos.
  - Ejemplo: `MiClase`, `ClaseEjemplo`.


- **Nombres de Funciones:**
  - Deben estar en minúsculas y las palabras separadas por guiones bajos (`_`).
  - Ejemplo: `calcular_promedio()`, `enviar_mensaje()`.


- **Espacios:**
  - Usar espacios alrededor de operadores (`+`, `-`, `*`, `/`, etc.) y después de comas.
  - Ejemplo: `x = 1 + 2`, `print(a, b)`.


## Hola Mundo en Python

En cualquier introducción a un nuevo lenguaje de programación, no puede faltar el famoso *Hola Mundo*. Se trata del primer programa por el que se empieza, que consiste en programar una aplicación que muestra por pantalla ese texto. Si ejecutas el siguiente código, habrás cumplido el primer hito de la programación en Python.

```python
print("Hola Mundo")
```

## Definiendo Variables en Python

Una variable es un espacio para almacenar datos modificables en la memoria de una computadora. Se define con la siguiente sintaxis:

```python
nombre_de_la_variable = valor_de_la_variable
```

Cada variable tiene un nombre y un valor, el cual define a la vez el tipo de datos de la variable.

Veamos un ejemplo: creemos una variable que almacene un número. A diferencia de otros lenguajes de programación, no es necesario decirle a Python el tipo de dato que queremos almacenar en x. Al ver el número 5, Python sabrá de qué tipo tiene que ser x. Sumamos un print para que muestre el valor asignado a la variable

```python
x = 5
print(x)
#Esperamos como salida del print un 5
```
## Constantes

Existe un tipo de «variable» denominada constante, la cual se utiliza para definir valores fijos que no requieran ser modificados.

Aunque Python no tiene un mecanismo incorporado para declarar constantes, se usa la convención de nombres para indicar que el valor es constante. Por eso, se definen en mayúsculas.

```python
PI = 3.14159
MAX_INTENTOS = 5
```
> Nota: Las constantes son una convención y no están protegidas por el lenguaje, por lo que se pueden modificar. Sin embargo, seguir esta convención ayuda a mantener el código más legible y estructurado.

### Comentarios

Los comentarios son bloques de texto usados para comentar el código. Es decir, para ofrecer a otros programadores o a nuestro yo futuro información relevante acerca del código que está escrito. A efectos prácticos, para Python es como si no existieran, ya que no son código propiamente dicho, solo anotaciones.

Los comentarios en Python se inician con `#` y todo lo que vaya después en la misma línea será considerado un comentario.

```python
# Esto es un comentario
```
Al igual que en otros lenguajes de programación, también podemos comentar varias líneas de código. Para ello es necesario hacer uso de triples comillas, ya sean simples (''') o dobles ("""). Es necesario usarlas para abrir el bloque del comentario y para cerrarlo.

```python
'''
Esto es un comentario
de varias líneas
de código
'''
```
**Comentarios Especiales**

Puedes usar comentarios especiales para marcar tareas o problemas en el código:
```python
# TODO: Esto es algo por hacer
# FIXME: Esto es algo que debe corregirse
# XXX: Esto también es algo que debe corregirse
```
> Según [PEP 8](https://peps.python.org/pep-0008/#comments), los comentarios en la misma línea del código deben separarse con **dos espacios en blanco**. 
> Ejemplo:
>```python
>a = 15  # Edad   OK
>a = 15 # Edad    NO
>```
## Tipos de Datos

Python soporta varios tipos de datos básicos y complejos. A continuación, se describen algunos de los tipos de datos más comunes en Python.

### Tipos Básicos

**Cadena de texto (string):**

```python
mi_cadena = "Hola Mundo!"
mi_cadena_multilinea = """Esta es una cadena
de varias líneas"""
```
**Número entero:**

```python
edad = 35
edad_oct = 0o43  # Notación octal
edad_hex = 0x23  # Notación hexadecimal
```
**Número real (float):**
```python
precio = 7435.28
```
**Booleano (bool):**
```python
verdadero = True
falso = False
```
## Tipos Complejos

### Tupla (tuple)

Una tupla es una variable que permite almacenar varios datos inmutables (no pueden ser modificados una vez creados) de tipos diferentes.

```python
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
```
Se puede acceder a cada uno de los datos mediante su índice correspondiente, siendo 0 el índice del primer elemento.
```python
print(mi_tupla[1])  # Salida: 15
```
También se puede acceder a una porción de la tupla, indicando (opcionalmente) desde el índice de inicio hasta el índice de fin.
```python
print(mi_tupla[1:4])  # Devuelve: (15, 2.8, 'otro dato')
print(mi_tupla[3:])   # Devuelve: ('otro dato', 25)
print(mi_tupla[:2])   # Devuelve: ('cadena de texto', 15)
```
Otra forma de acceder a la tupla es de forma inversa (de atrás hacia adelante), utilizando índices negativos.
```python
print(mi_tupla[-1])  # Salida: 25
print(mi_tupla[-2])  # Salida: 'otro dato'
```
### Lista (list)

Las listas permiten almacenar elementos de diferentes tipos y modificar sus valores.

```python
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
mi_lista[2] = 2.8
```
Las listas **NO** son inmutables: permiten modificar los datos una vez creados.
```python
mi_lista[2] = 3.8  # El tercer elemento ahora es 3.8
```
Además, las listas permiten agregar nuevos valores, a diferencia de las tuplas.
```python
mi_lista.append('Nuevo Dato')
```
### Diccionario (dict)

Mientras que a las listas y tuplas se accede solo por un índice numérico, los diccionarios permiten utilizar una clave para declarar y acceder a un valor.

```python
mi_diccionario = {'clave_1': 'valor_1', 'clave_2': 'valor_2'}
print(mi_diccionario['clave_2'])  # Salida: valor_2
```
Un diccionario permite eliminar cualquier entrada utilizando la palabra clave `del`.
```python
del mi_diccionario['clave_2']
```
Al igual que las listas, los diccionarios permiten modificar los valores asociados a una clave.
```python
mi_diccionario['clave_1'] = 'Nuevo Valor'
```

## Operadores

Python ofrece varios operadores para realizar operaciones aritméticas, comparativas y lógicas.

### Operadores Aritméticos

- `+` Suma
- `-` Resta
- `*` Multiplicación
- `/` División
- `//` División entera
- `%` Módulo
- `**` Potenciación

**Ejemplo de uso:**

```python
monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
```
### Operadores Comparativos

- `==` Igualdad
- `!=` Desigualdad
- `>` Mayor que
- `<` Menor que
- `>=` Mayor o igual que
- `<=` Menor o igual que

**Ejemplo de uso:**

```python
if edad >= 18:
    print("Eres mayor de edad")
```
### Operadores Lógicos

- `and` Conjunción
- `or` Disyunción
- `not` Negación

**Ejemplo de uso:**

```python
if (edad >= 18) and (nacionalidad == 'argentina'):
    print("Eres mayor de edad y eres argentino")
```
> PEP 8: Operadores
> Siempre colocar un espacio en blanco antes y después de un operador para mejorar la legibilidad del código.
> Para más detalles, puedes consultar la sección sobre operadores en la [PEP 8](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements).
> 
>**Ejemplo:**
> ```python
> # Correcto
> a = 5 + 3
> # Incorrecto
> a=5+3
> ```
