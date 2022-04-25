from Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        self.deck = [Card(v, s) for v in Card.value_list for s in Card.suit_list]

    def __str__(self):
        return f'Main deck: {self.deck}'

    def cards_shuffle(self):
        """Shuffles the main deck"""
        shuffle(self.deck)

    def deal_one(self):
        """Returns a random card from the deck and removes it"""
        a = choice(self.deck)
        self.deck.remove(a)
        return a


if __name__ == "__main__":
    my_deck = DeckOfCards()
    print(my_deck)
    # DeckOfCards.cards_shuffle(my_deck)
    # print("Shuffle", my_deck)
    # my_deck.deal_one()
    print(my_deck.deal_one())

    # print(choice(my_deck))
    print(my_deck)
