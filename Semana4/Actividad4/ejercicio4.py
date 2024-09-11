'''
4. Escribir un programa que solicite el ingreso de un número entero y, si el número
leído es par, imprima la leyenda 'El número es PAR'. En caso contrario, deberá
mostrar el texto 'El número es IMPAR'
'''

# Solicitamos el ingreso de un numero entero
numero = int(input("Ingrese un número entero: "))

#Verificamos con % (operador modulo) el cual se utiliza para obtener el resto de una division, comparamos y mostramos si el numero es par o impar.
if numero % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")
