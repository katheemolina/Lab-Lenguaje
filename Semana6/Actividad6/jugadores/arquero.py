from jugadores.jugador import Jugador

class Arquero(Jugador):
    def __init__(self, numero_camisa, apellido):
        super().__init__(numero_camisa, apellido, "Arquero")
