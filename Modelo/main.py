import random
from Carta import Carta

def crearBaraja():
    valorCarta = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    paloCarta = ["t", "c", "p", "r"]
    baraja = []

    for n in valorCarta:
        for p in paloCarta:
            carta = Carta(n,p)
            baraja.append(carta)
    return baraja

def takeCard(baraja):
    carta = baraja.pop()
    print("Carta seleccionada: " + str(carta))
    # cartasRestanantes = baraja.count()
    # print("En la baraja quedan " + cartasRestanantes)

def iniciar():
    baraja = crearBaraja()
    random.shuffle(baraja)
    takeCard(baraja)

def menu():
    print("1 - Coger Carta"
          "2 - Salir")



iniciar()