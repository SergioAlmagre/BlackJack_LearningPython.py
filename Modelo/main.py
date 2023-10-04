from Player import Player
from Modelo.Game import Game

def numberOfPlayers():
    totalPlayers = []
    numberIntPlayers = 0
    humanNumber = 0

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

        human = input("Is human this player? \n0 - NO\n1 - YES\n")
        try:
            humanNumber = int(human)
            correct = True
        except ValueError:
            print("Something was wrong, try to put a new value again\n")

        newPlayer = Player(namePlayer, humanNumber)
        totalPlayers.append(newPlayer)
    return totalPlayers


def askToExit():
    exit = False
    answer = input(" Do you want to exit? \n Y/N\n").upper().strip()
    if answer == "Y":
        exit = True

    return exit



def start():
    exit = False

    while not exit:
        winner = False
        nPlayers = numberOfPlayers()
        blackJack = Game(nPlayers)

        blackJack.shuffleCards()
        blackJack.randomTurn()

        while not winner:
            blackJack.changeTurn()
            blackJack.takeCard()
            blackJack.checkCards()
            print(blackJack)
            winner = blackJack.checkWinners()

        exit = askToExit()


start()