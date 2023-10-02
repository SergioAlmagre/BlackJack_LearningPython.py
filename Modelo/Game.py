import random
import Card
import Player
class Game:

    def crearBaraja(self):
        valorCarta = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        paloCarta = ["t", "c", "p", "r"]
        baraja = []

        for n in valorCarta:
            for p in paloCarta:
                card = Card(n, p)
                baraja.append(card)
        return baraja




    def shuffleCards(self):
        random.shuffle(self.baraja)

