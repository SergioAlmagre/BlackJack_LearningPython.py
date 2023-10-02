class Card:

    def __init__(self, valor, letra):
        self.valor = valor
        self.letra = letra

    def __str__(self):
        return f"{self.valor}{self.letra}"


