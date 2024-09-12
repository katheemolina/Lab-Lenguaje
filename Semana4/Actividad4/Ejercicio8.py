def suma_numeros():
    cantidad = int(input("Ingrese la cantidad de números a procesar: "))
    suma_total = 0
    
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        suma_total += numero
    
    print(f"La suma total de los números ingresados es: {suma_total}")

suma_numeros()