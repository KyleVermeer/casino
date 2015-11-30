import unittest
from blackjack.card import *

class TestCard(unittest.TestCase):

    def test_constructor(self):

        # Test the constructor
        card = PlayingCard(Rank.Two, Suit.Heart)

        # Assertions
        self.assertEqual(card.getRank(), Rank.Two, ('Rank should match the rank'
                                                    ' provided to contructor.'))
        self.assertEqual(card.getSuit(), Suit.Heart, ('Suit should match the suit'
                                                      ' provided to the constructor.'))
        self.assertFalse(card.getFaceDown(), 'Card should be face up.')

    def test_setFaceDown(self):

        # Set up data
        card = PlayingCard(Rank.Ace, Suit.Club)

        # Test the setFaceDown method
        isFaceDown = card.setFaceDown(True)

        # Assertions
        self.assertTrue(card.getFaceDown(), 'Card should be face down.')
