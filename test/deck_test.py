import unittest
from blackjack.deck import *

class TestDeck(unittest.TestCase):

    def test_deckConstructor(self):

        # Test the constructor
        myDeck = Deck()

        # Assertions
        self.assertFalse(myDeck.hasCards(), 'A plain deck should have no cards upon initialization.')

    def test_fiftyTwoCardDeckConstructor(self):

        # Test the constructor
        myDeck = FiftyTwoCardDeck()

        # Assertions
        self.assertTrue(myDeck.hasCards(), 'A fifty card deck should have cards upon initialization.')
