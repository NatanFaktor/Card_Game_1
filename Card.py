class Card:
    value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
    suit_list = ["Diamonds", "Spades", "Hearts", "Clubs"]

    def __init__(self, value, suit):
        if type(value) != int:
            raise TypeError("Argument value must be int")
        if type(suit) != str:
            raise TypeError("Argument suit must be str")
        if value in self.value_list:
            self.value = value
        else:
            raise ValueError("Value not in range")
        if suit in self.suit_list:
            self.suit = suit
        else:
            raise ValueError("Suit not defined")

    def __repr__(self):
        if self.value == 1:
            return f"{'Ace'} of {self.suit}"
        elif self.value == 13:
            return f"{'King'} of {self.suit}"
        elif self.value == 12:
            return f"{'Queen'} of {self.suit}"
        elif self.value == 11:
            return f"{'Jack'} of {self.suit}"
        else:
            return f"{self.value} of {self.suit}"

    def __gt__(self, other):
        """Gets two cards and returns True if the first one is grater then the other"""
        if type(other) != Card:
            return TypeError("Other argument must be type Card")
        if self.value != other.value:
            return self.value_list.index(self.value) > other.value_list.index(other.value)
        else:
            return self.suit_list.index(self.suit) > other.suit_list.index(other.suit)

    def __eq__(self, other):
        if type(other) != Card:
            return TypeError('Other object must be card type')
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False


if __name__ == "__main__":
    card1 = Card(1, "Diamonds")
    print(card1)
    # print("Clubs index", card1.suit_list.index("Clubs"))
    # print("Spades index", card1.suit_list.index("Spades"))

    card2 = Card(9, "Spades")
    print(card2)
    print(card1 > card2)
