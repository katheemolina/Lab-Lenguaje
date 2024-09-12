def procesar_numeros():
    suma_negativos = 0
    suma_positivos = 0
    cantidad_positivos = 0
    
    for i in range(8):
        while True:
            numero = int(input(f"Ingrese el número {i + 1} (entre -10 y 10): "))
            
            if -10 <= numero <= 10:
                break
            else:
                print("Número fuera del rango. Inténtelo de nuevo.")
        
        if numero <= 0:
            suma_negativos += numero
        else:
            suma_positivos += numero
            cantidad_positivos += 1
    
    promedio_positivos = suma_positivos / cantidad_positivos if cantidad_positivos > 0 else 0
    
    print(f"La suma de los valores negativos es: {suma_negativos}")
    print(f"El promedio de los valores positivos es: {promedio_positivos}")

procesar_numeros()