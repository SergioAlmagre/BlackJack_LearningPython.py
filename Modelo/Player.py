from Card import Carta
class Jugador:

    def __init__(self, machine, turn, points, deckOfCards):
        self.machine = machine
        self.turn = turn
        self.points = points
        self.deckOfCards = deckOfCards

    def __str__(self):
        return f"{self.cartas}{self.puntos}"

    def takeCard(baraja):
        carta = baraja.pop()
        print("Carta seleccionada: " + str(carta))
        # cartasRestanantes = baraja.count()
        # print("En la baraja quedan " + cartasRestanantes)

    def sumarCartas(self, player):
        for carta in self.cartas:
            self.puntos += carta.valor
        return self.puntos

