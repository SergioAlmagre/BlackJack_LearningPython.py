from DeckOfCards import DeckOfCards

class Player:
    def __init__(self, name,human):
        self.name = name
        self.turn = 0
        self.points = 0
        self.human = human
        self.stand = False
        self.winner = True
        self.deckOfCards = DeckOfCards()

    def sumValues(self):
        total = 0

        card_values = {  # Define un diccionario que mapea los valores de las cartas a sus valores numéricos
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10
        }

        for i in self.deckOfCards.cards:
            cardStr = i.value[0] # Toma solo el primer carácter del valor de la carta
            self.points += card_values.get(cardStr, i)  # Obtiene el valor de la carta a partir del diccionario

        return self.points




    def __str__(self):
        return f"Name: {self.name} Turn: {self.turn} Point: {self.points} Cards: {self.deckOfCards}\n"


