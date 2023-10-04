from DeckOfCards import DeckOfCards

class Player:
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.point = 0
        self.human = 0
        self.stand = False
        self.winner = True
        self.deckOfCards = DeckOfCards()

    def sumValues(self):
        total = 0
        for i in self.deckOfCards:
            total += i.value
            return total




    def __str__(self):
        return f"Name: {self.name}, Turn: {self.turn}, Point: {self.point}"


