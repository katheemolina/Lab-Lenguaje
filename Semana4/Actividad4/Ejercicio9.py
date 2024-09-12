def suma_numeros_modificado():
    cantidad = int(input("Ingrese la cantidad de números a procesar: "))
    suma_total = 0
    suma_pares = 0
    suma_impares = 0
    
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        if numero >= 0:
            suma_total += numero
            if numero % 2 == 0:
                suma_pares += numero
            else:
                suma_impares += numero
    
    print(f"La suma total de los números ingresados es: {suma_total}")
    print(f"La suma de los números positivos pares es: {suma_pares}")
    print(f"La suma de los números positivos impares es: {suma_impares}")

suma_numeros_modificado()