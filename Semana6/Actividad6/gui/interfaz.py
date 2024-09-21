from jugadores.arquero import Arquero
from jugadores.defensor import Defensor
from jugadores.central import Central
from jugadores.delantero import Delantero
jugadores = []

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Cargar Jugador")
    print("2. Consultar Estadísticas")
    print("3. Salir")

def cargar_jugador():
    numero = input("Ingrese el número de camiseta: ")
    apellido = input("Ingrese el apellido: ")
    posicion = input("Ingrese la posición (Arquero, Defensor, Central, Delantero): ").lower()

    match posicion:
        case "arquero":
            jugador = Arquero(numero, apellido)
        case "defensor":
            jugador = Defensor(numero, apellido)
        case "central":
            jugador = Central(numero, apellido)
        case "delantero":
            jugador = Delantero(numero, apellido)
        case _:
            print("Posición no válida. El jugador no se cargó.")

    jugadores.append(jugador)
    print(f"Jugador {apellido} cargado exitosamente.")

def consultar_estadisticas():
    if not jugadores:
        print("No hay jugadores cargados.")
        return
    
    print("\n--- Estadísticas de los Jugadores ---")
    for jugador in jugadores:
        print(jugador.mostrar_estadisticas())

def iniciar_aplicacion():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                cargar_jugador()
            case "2":
                consultar_estadisticas()
            case "3":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")