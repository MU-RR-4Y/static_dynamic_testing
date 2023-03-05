import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card('spades', 9)
        self.card2 = Card('diamonds', 5)

    def test_card_suit(self):
        self.assertEqual('spades', self.card.suit)

    def test_card_value(self):
        self.assertEqual(9, self.card.value)

    def test_check_for_ace(self):
        result = CardGame.check_for_ace(self, self.card)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = CardGame.highest_card(self, self.card, self.card2)
        self.assertEqual(self.card, result)

    def test_card_total(self):
        cards =[self.card, self.card2]
        result = CardGame.cards_total(self, cards)
        self.assertEqual('You have a total of 14', result)