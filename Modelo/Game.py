import random

from Modelo.Card import Card
from Modelo.DeckOfCards import DeckOfCards
from Modelo.Player import Player


class Game:
    def __init__(self,players):
        self.players = players
        self.deckOfCards = self.createDeckOfCards()

    def createDeckOfCards(self):
        cardValue = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
        cardSuit = ["t", "c", "p", "r"]
        mainDeckOfCards = DeckOfCards()

        for n in cardValue:
            for p in cardSuit:
                card = Card(n, p)
                mainDeckOfCards.cards.append(card)
        return mainDeckOfCards


    def shuffleCards(self):
        random.shuffle(self.deckOfCards.cards)

    def takeCard(self):
        for i in self.players:
            if i.turn == 1:
                if not i.stand:
                    if i.human == 0:
                        card = self.deckOfCards.cards.pop()
                        print(card)
                        i.deckOfCards.cards.append(card)
                    else:
                        total = i.sumValues()
                        print("Your total is ", total, "\n")
                        answer = input(" Do you want to take one more? \n Y/N\n").upper().strip()
                        if answer == "Y":
                            card = self.deckOfCards.cards.pop()
                            print(card)
                            i.deckOfCards.cards.append(card)
                        else:
                            i.stand = True
                            print(f"The game continue whithout {i.name}!")


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
                if not i.stand:
                    total = i.sumValues()
                    if i.human == 0:
                        if total >= 17 and total <= 21:
                            i.stand = True
                        elif total > 21:
                            i.stand = True
                            i.winner = False
                    else:
                        if total > 21:
                            i.stand = True
                            i.winner = False
                        else:
                            print("Your total is ", total, "\n")
                            answer = input(" Do you want to stand? \n Y/N\n").upper().strip()
                            if answer == "Y":
                                i.stand = True
                            else:
                                print("The game continue!")

    def checkWinners(self):
        allStanded = True
        isThereWinner = False
        winner = None
        for i in self.players:
            if not i.stand:
                allStanded = False

        if allStanded:
            for i in self.players:
                if i.winner:
                    winner = i
                    break
            for i in self.players:
                if i.winner:
                    if i.points > winner.points:
                        winner = i
            isThereWinner = True

            if winner is not None:
                print(f"The winner is {winner.name} with {winner.points}!!!!\n")
            else:
                print("Everyone losed!.\n")
            return isThereWinner


    def __str__(self):
        players_str = "".join(str(player) for player in self.players)
        # cards_str = str(self.deckOfCards)
        return f"{players_str}\n"

















