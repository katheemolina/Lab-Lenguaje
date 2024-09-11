'''
7. Solicitar el ingreso de un número entero. Si el número ingresado es impar,
se deberán imprimir los números correlativos desde el ingresado hasta el doble
del mismo. Si el número ingresado es par, se deberán mostrar los números pares
desde el ingresado hasta el doble del ingresado. Por ejemplo: si se ingresa un 8,
se mostrará 8, 10, 12, 14, 16. Si se ingresa un 5, se mostrarán 5, 6, 7, 8, 9, 10.
'''

# Solicita al usuario que ingrese un numero entero
numero = int(input("Ingrese un número entero: "))

# Verifica si el numero es impar
if numero % 2 != 0:
    # Imprime numeros correlativos desde el ingresado hasta el doble del mismo
    for i in range(numero, numero * 2 + 1):
        print(i, end=", ")
else:
    # Imprime numeros pares desde el ingresado hasta el doble del ingresado
    for i in range(numero, numero * 2 + 1):
        if i % 2 == 0:
            print(i, end=", ")
