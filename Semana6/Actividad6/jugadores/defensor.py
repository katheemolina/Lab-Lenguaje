from jugadores.jugador_con_goles import JugadorConGoles

class Defensor(JugadorConGoles):
    def __init__(self, numero_camisa, apellido):
        super().__init__(numero_camisa, apellido, "Defensor")
