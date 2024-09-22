import tkinter as tk
from tkinter import messagebox
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

def cargar_jugador_menu():
    global txtNumero, txtApellido, txtPosicion, txtMinutos

    rootplayer = tk.Tk()
    rootplayer.title("Cargar Jugador")
    rootplayer.geometry("500x500")
    rootplayer.configure(bg="#d1e0ab")


    lblNumero = tk.Label(rootplayer,text="Ingrese el número de camiseta: ")
    lblNumero.pack(pady=5)
    txtNumero = tk.Entry(rootplayer)
    txtNumero.pack(pady=5)

    lblApellido = tk.Label(rootplayer,text="Ingrese el apellido: ")
    lblApellido.pack(pady=5)
    txtApellido = tk.Entry(rootplayer)
    txtApellido.pack(pady=5)

    lblPosicion = tk.Label(rootplayer,text="Ingrese la posición (Arquero, Defensor, Central, Delantero): ")
    lblPosicion.pack(pady=5)
    txtPosicion = tk.Entry(rootplayer)
    txtPosicion.pack(pady=5)

    lblMinutos = tk.Label(rootplayer,text="Ingrese los minutos jugados: ")
    lblMinutos.pack(pady=5)
    txtMinutos = tk.Entry(rootplayer)
    txtMinutos.pack(pady=5)

    btnGuardar = tk.Button(rootplayer,text="Guardar Jugador",command=cargar_jugador)
    btnGuardar.pack(pady=10)




def cargar_jugador():
    posicion = txtPosicion.get().lower()  # Convertir a minúsculas para evitar problemas con el case
    numero = txtNumero.get()
    apellido = txtApellido.get()
    minutos = txtMinutos.get()

    jugador = None

    match posicion:
        case "arquero":
            jugador = Arquero(numero, apellido, minutos)
        case "defensor":
            jugador = Defensor(numero, apellido, minutos)
        case "central":
            jugador = Central(numero, apellido, minutos)
        case "delantero":
            jugador = Delantero(numero, apellido, minutos)
        case _:
            messagebox.showerror("Error", "Posición no válida. El jugador no se cargó.")
    
    # Si el jugador fue creado (posición válida), se agrega a la lista
    if jugador:
        jugadores.append(jugador)
        messagebox.showinfo("Éxito", f"Jugador {apellido} cargado exitosamente.")
        limpiar_campos() ## Limpio los inputs



def limpiar_campos():
    txtNumero.delete(0, tk.END)  
    txtApellido.delete(0, tk.END)
    txtPosicion.delete(0, tk.END)
    txtMinutos.delete(0, tk.END)



def consultar_estadisticas():
    if not jugadores:
        messagebox.showinfo("Alerta", "No hay jugadores cargados.")
        return

    estadisticas = "Lista de jugadores:\n"
    
    for jugador in jugadores:
        estadisticas += jugador.mostrar_estadisticas() + "\n" 

    # Mostrar todas las estadísticas en un solo messagebox
    messagebox.showinfo("Estadísticas", estadisticas)


