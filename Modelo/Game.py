import random

from Modelo.Card import Card
from Modelo.DeckOfCards import DeckOfCards
from Modelo.Player import Player


class Game:
    def __init__(self,players):
        self.players = players
        self.deckOfCards = self.createDeckOfCards()

    def createDeckOfCards(self):
        cardValue = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuit = ["t", "c", "p", "r"]
        mainDeckOfCards = DeckOfCards()

        for n in cardValue:
            for p in cardSuit:
                card = Card(n, p)
                mainDeckOfCards.cards.append(card)
        return mainDeckOfCards


    def shuffleCards(self, deckOfCards):
        random.shuffle(deckOfCards.cards)

    def takeCard(self):
        card = self.deckOfCards.cards.pop()
        return card

    def changeTurn(self):
        for i in range(0, len(self.players)):
            if self.players[i].turn == 1:
                self.players[i].turn = 0
                next_index = (i + 1) % len(self.players)  # Patron circular para conocer el índice del siguiente jugador
                self.players[next_index].turn = 1
                break


    def randomTurn(self):
        num = random.randrange(0, len(self.players))
        self.players[num].turn = 1


    def checkCards(self):
        total = 0
        for i in self.players:
            if i.turn == 1:
                total = i.sumValues()
                if total > 17 & total < 21:
                    i.stand = True
                print(total)

    def __str__(self):
        players_str = ", ".join(str(player) for player in self.players)
        # cards_str = str(self.deckOfCards)
        return f"Players: {players_str}\nCards:"

















