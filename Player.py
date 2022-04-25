from DeckOfCards import *
from random import *


class Player:
    def __init__(self, player_name: str, num_cards: int = 26):
        if type(player_name) != str:
            raise TypeError("Argument player_name must be str")
        if type(num_cards) != int:
            raise TypeError("Argument num_cards must be int")
        self.player_name = player_name
        self.num_cards = num_cards
        if self.num_cards < 10 or self.num_cards > 26:
            self.num_cards = 26
        self.player_deck = []

    def __str__(self):
        return f"{self.player_name} with {len(self.player_deck)} cards"

    def set_hand(self, deck: DeckOfCards):
        """Gets a full deck and adds cards to players hand based on num_cards"""
        if type(deck) != DeckOfCards:
            raise TypeError("Argument deck must be DeckOfCards")
        for i in range(self.num_cards):
            self.player_deck.append(deck.deal_one())

        # print(my_deck.deck)

    def get_card(self):
        """Returns a random card from the players hand and removes it"""
        rand_choice = choice(self.player_deck)
        self.player_deck.remove(rand_choice)
        return rand_choice

    def add_card(self, card: Card):
        """Adds a card to a players hand"""
        if type(card) != Card:
            raise TypeError("Argument must be Card")
        if card in self.player_deck:
            return 'Card is already in player deck'
        self.player_deck.append(card)


if __name__ == "__main__":
    my_deck = DeckOfCards()
    print("1", my_deck)
    p1 = Player("Natan", 20)
    p2 = Player("Gavriel", 20)
    print(p1.player_deck)
    print(p2.player_deck, "\n")

    p1.set_hand(my_deck)
    p2.set_hand(my_deck)
    print("2", my_deck)
    # print("P1", p1.player_deck)
    # print("Get Card", p1.get_card(), "\n")
    print(len(p1.player_deck))
    print("P1", p1.player_deck)
    print(len(p2.player_deck))
    print("P2", p2.player_deck, "\n")
    # p1.add_card(Card(11, "Diamonds"))
    # print("Add Card p1", p1.player_deck)
    print(p1)
    print(p2)
