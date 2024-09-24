from gui.interfaz import cargar_jugador, cargar_jugador_menu, consultar_estadisticas, agregar_goles
import tkinter as tk
from tkinter import Menu, messagebox

def about():
    messagebox.showinfo("Acerca de", "Esta es una aplicación hecha por el grupo 8.")

def exit_app():
    messagebox.showinfo("Salida", "Gracias por usar el sistema")
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestion de Jugadores")
root.geometry("300x300")
root.configure(bg="#d1e0ab")

# Crear un menú
menu_bar = Menu(root)

# Crear un menú "Ayuda"
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Acerca de", command=about)
menu_bar.add_cascade(label="Ayuda", menu=help_menu)

# Configurar la barra de menú
root.config(menu=menu_bar)

btnCargarJugador = tk.Button(root, text ="Cargar un jugador", command=cargar_jugador_menu)
btnCargarJugador.pack(pady=5)

btnEstadisticas = tk.Button(root, text ="Consultar estadisticas", command=consultar_estadisticas)
btnEstadisticas.pack(pady=5)

btnAgregarGoles = tk.Button(root, text ="Agregar Goles", command=agregar_goles)
btnAgregarGoles.pack(pady=5)

btnSalir = tk.Button(root, text ="Salir del sistema", command=exit_app)
btnSalir.pack(pady=5)


# Iniciar el bucle de eventos
root.mainloop()

