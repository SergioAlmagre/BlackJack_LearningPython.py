class Jugador:

    def __init__(self, maquina, turno, puntos, cartas = []):
        self.maquina = maquina
        self.turno = turno
        self.cartas = []
        self.puntos = puntos

    def __str__(self):
        return f"{self.cartas}{self.puntos}"

    def sumarCartas(self):
        res = 0
        for c in self.cartas:
            puntos = puntos + c.valor
