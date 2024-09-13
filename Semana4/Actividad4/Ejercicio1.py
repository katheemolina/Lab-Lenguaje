#Programa 1:
# Escribir un programa que solicite el ingreso de dos números enteros y que
#imprima el resultado de la suma, resta, multiplicación, cociente y resto de la
#división.

n1 = float(input("Ingrese el primer numero:"))
n2 = float(input("Ingrese el segundo numero:"))

suma = n1 + n2
print("El resultado de la suma es: ", suma)

resta = n1 - n2
print("El resultado de la resta es: ",resta)

if n2 != 0:
    cociente = n1 // n2
    resto = n1 % n2
    
    # Mostrar los resultados
    print(f"El cociente de {n1} dividido por {n2} es: {cociente}")
    print(f"El resto de {n1} dividido por {n2} es: {resto}")
else:
    print("No se puede dividir por cero.")

multiplicacion = n1 * n2
print("El resultado de la multiplicacion es: ", multiplicacion)



