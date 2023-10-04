from Player import Player
from Modelo.Game import Game

def menu():
    print("1 - Coger Carta"
          "2 - Salir")

def numberOfPlayers():
    totalPlayers = []
    numberIntPlayers = 0

    correct = False
    while not correct:
        numberStringPlayers = input("How many players play?\n")
        try:
            numberIntPlayers = int(numberStringPlayers)
            correct = True
        except ValueError:
            print("Something was wrong, try to put a new value again\n")

    for i in range(1, numberIntPlayers + 1):
        namePlayer = input("What is the name of the new player number " + str(i) + "\n")
        newPlayer = Player(namePlayer)
        totalPlayers.append(newPlayer)
    return totalPlayers





def init():

    nPlayers = numberOfPlayers()

    blackJack = Game(nPlayers)
    # print(blackJack)
    blackJack.randomTurn()
    print(blackJack)
    blackJack.checkCards()

    blackJack.changeTurn()
    print(blackJack)

    newCard = blackJack.takeCard()
    print(newCard)


    #
    # blackJack.shuffleCards(blackJack.deckOfCards)
    # print(blackJack.deckOfCards)




init()