#3. Modificar el programa anterior para que ahora solicite el ingreso de dos números
#enteros, y que luego informe si el primero es o no mayor que el segundo, usando
#el formato 'X es mayor que Y' (o ‘X no es mayor que Y’). Si ambos números fueran
#iguales, deberá informar 'X es igual a Y'. Por ejemplo, si se ingresan 23 y 42, se
#mostraría '42 es mayor que 23'.

numero = int(input("Ingrese un numero X: "))
numero2 = int(input("Ingrese un numero Y: "))

if numero > numero2: print(numero, " es mayor a ", numero2)
elif numero < numero2: print(numero, " no es mayor a ", numero2)
else: print(numero, " es igual a ", numero2)
