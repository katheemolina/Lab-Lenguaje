'''
5. Solicitar al usuario que ingrese el día de la semana y la cantidad de artículos
comprados por un cliente en un comercio. Finalmente, imprimir “accede al
descuento” si el día es lunes y el cliente compró más de 3 artículos. En caso
contrario, no imprimir nada.
'''

# Solicitamos al usuario que ingrese el dia de la semana y la cantidad de articulos comprados
# .lower() es un metodo que convierte los caracteres de la cadena texto a minusculas para mitigar errores al introducir el texto solicitado
dia = input("Ingrese el dia de la semana: ").lower()
cantidad_articulos = int(input("Ingrese la cantidad de articulos comprados: "))

# Verificar si el dia es lunes y si la cantidad de articulos es mayor a 3
if dia == "lunes" and cantidad_articulos > 3:
    print("Accede al descuento")
