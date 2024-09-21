from jugadores.jugador import Jugador

class JugadorConGoles(Jugador):
    def __init__(self, numero_camisa, apellido, posicion):
        super().__init__(numero_camisa, apellido, posicion)
        self.goles_marcados = 0

    def marcar_gol(self):
        self.goles_marcados += 1

    def mostrar_estadisticas(self):
        estadisticas = super().mostrar_estadisticas()
        return f"{estadisticas}, Goles: {self.goles_marcados}"
