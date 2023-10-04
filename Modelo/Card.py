class Card:
    def __init__(self, value, letter):
        self.value = value
        self.letter = letter

    def __str__(self):
        return f"{self.value}{self.letter}"


