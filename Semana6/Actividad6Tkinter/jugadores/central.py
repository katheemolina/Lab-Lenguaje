from jugadores.jugador_con_goles import JugadorConGoles

class Central(JugadorConGoles):
    def __init__(self, numero_camisa, apellido, minutos):
        super().__init__(numero_camisa, apellido, "Central", minutos)
