from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card
from unittest import TestCase, mock
from unittest.mock import patch


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.mydeck = DeckOfCards()
        print(self.mydeck)

    def test__init__(self):
        self.assertTrue(type(self.mydeck) is DeckOfCards)

    def test_cards_shuffle(self):
        self.mydeck2 = DeckOfCards()
        self.mydeck2.cards_shuffle()

        self.assertNotEqual(self.mydeck, self.mydeck2)

    def test_deal_one(self):
        a = DeckOfCards.deal_one(self.mydeck)
        self.assertEqual(len(self.mydeck.deck), 51)
        self.assertNotIn(a, self.mydeck.deck)







