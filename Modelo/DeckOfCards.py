class DeckOfCards:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)