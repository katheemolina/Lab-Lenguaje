import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from jugadores.arquero import Arquero
from jugadores.defensor import Defensor
from jugadores.central import Central
from jugadores.delantero import Delantero
from jugadores.jugador_con_goles import JugadorConGoles

jugadores = []

def cargar_jugador_menu():
    global txtNumero, txtApellido, ddlPosicion, txtMinutos

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
    ddlPosicion = ttk.Combobox(rootplayer,
                               values = ("Arquero", "Defensor", "Central", "Delantero"),
                               state="readonly")
    ddlPosicion.set("Arquero") 
                               
    ddlPosicion.pack(pady=5)
    
    lblMinutos = tk.Label(rootplayer,text="Ingrese los minutos jugados: ")
    lblMinutos.pack(pady=5)
    txtMinutos = tk.Entry(rootplayer)
    txtMinutos.pack(pady=5)

    btnGuardar = tk.Button(rootplayer,text="Guardar Jugador",command=cargar_jugador)
    btnGuardar.pack(pady=10)



def cargar_jugador():
    posicion = ddlPosicion.get().lower()  # Convertir a minúsculas para evitar problemas con el case
    numero = txtNumero.get()
    apellido = txtApellido.get()
    minutos = txtMinutos.get()

    if not numero.isdigit():
        messagebox.showerror("Error", "Asegúrese de ingresar un número de camiseta válido.")
        return
    if not apellido:
        messagebox.showerror("Error", "Asegúrese de ingresar un apellido válido.")
        return
    if not minutos.isdigit():
        messagebox.showerror("Error", "Asegúrese de ingresar un número de minutos válido.")
        return
    
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
    ddlPosicion.delete(0, tk.END)
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



def agregar_goles():
    global txtGoles
    # Crear la ventana principal
    rootAgregarGoles = tk.Tk()
    rootAgregarGoles.title("Agregar Goles")
    rootAgregarGoles.geometry("300x300")
    rootAgregarGoles.configure(bg="#d1e0ab")
    
    jugadores_apellidos = [jugador.apellido for jugador in jugadores]
    
    lblJugador = tk.Label(rootAgregarGoles, text="Seleccione el jugador: ")
    lblJugador.pack(pady=5)
    ddlJugador = ttk.Combobox(rootAgregarGoles, values=jugadores_apellidos, state="readonly")
    ddlJugador.pack(pady=5)
    
    lblGoles = tk.Label(rootAgregarGoles, text="Ingrese la cantidad de goles: ")
    lblGoles.pack(pady=5)
    txtGoles = tk.Entry(rootAgregarGoles)
    txtGoles.pack(pady=5)
    
    btnAgregarGoles = tk.Button(rootAgregarGoles, text="Agregar Goles", command=lambda: guardar_goles(ddlJugador.get(), txtGoles.get()))
    btnAgregarGoles.pack(pady=10)



def guardar_goles(apellido, goles_str):
    if not apellido or not goles_str.isdigit():
        messagebox.showerror("Error", "Seleccione un jugador y asegúrese de ingresar un número de goles válido.")
        return

    goles = int(goles_str)
    for jugador in jugadores:
        if jugador.apellido == apellido:
            if isinstance(jugador, JugadorConGoles):
                for _ in range(goles):
                    jugador.marcar_gol()
                messagebox.showinfo("Éxito", f"{goles} goles agregados a {jugador.apellido}.")
            else:
                messagebox.showerror("Error", f"{jugador.apellido} no es un jugador que puede marcar goles.")
            break
    else:
        messagebox.showerror("Error", "Jugador no encontrado.")
        
    txtGoles.delete(0, tk.END)