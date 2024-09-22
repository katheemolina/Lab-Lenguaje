class Jugador:
    def __init__(self, numero_camisa, apellido, posicion, minutos_jugados=0):
        self.numero_camisa = numero_camisa
        self.apellido = apellido
        self.posicion = posicion
        self.minutos_jugados = minutos_jugados

    def jugar_minutos(self, minutos):
        self.minutos_jugados += minutos

    def mostrar_estadisticas(self):
        return f"Jugador: {self.apellido}, Camiseta: {self.numero_camisa}, Posición: {self.posicion}, Minutos Jugados: {self.minutos_jugados}"
