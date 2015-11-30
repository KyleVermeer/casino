import unittest
from blackjack.blackjack import *
from blackjack.card import *

class BlackJackTestCase(unittest.TestCase):

    def test_handGetCountKingTwo(self):

        # Create Hand
        myHand = Hand(None)

        twoOfHearts = PlayingCard(Rank.Two, Suit.Heart)
        kingOfSpades = PlayingCard(Rank.King, Suit.Spade)

        myHand.addCard(twoOfHearts)
        myHand.addCard(kingOfSpades)

        # Test getCount
        count = myHand.getCount()

        # Assertions
        self.assertEqual(count, 12, ('Count for King and Two should be 12.'))

    def test_handGetCountKingAce(self):

        # Create Hand
        myHand = Hand(None)

        aceOfHearts = PlayingCard(Rank.Ace, Suit.Heart)
        kingOfSpades = PlayingCard(Rank.King, Suit.Spade)

        myHand.addCard(aceOfHearts)
        myHand.addCard(kingOfSpades)

        # Test getCount
        count = myHand.getCount()

        # Assertions
        self.assertEqual(count, 21, ('Count for King and Ace should be 21.'))

    def test_handGetCountKingSixAce(self):

        # Create Hand
        myHand = Hand(None)

        sixOfHearts = PlayingCard(Rank.Six, Suit.Heart)
        kingOfSpades = PlayingCard(Rank.King, Suit.Spade)
        aceOfDiamonds = PlayingCard(Rank.Ace, Suit.Diamond)

        myHand.addCard(sixOfHearts)
        myHand.addCard(kingOfSpades)
        myHand.addCard(aceOfDiamonds)

        # Test getCount
        count = myHand.getCount()

        # Assertions
        self.assertEqual(count, 17, ('Count for King, Six, and Ace should be 17.'))
