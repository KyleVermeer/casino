import unittest
from test.card_test import TestCard
from test.deck_test import TestDeck
from test.blackjack_test import BlackJackTestCase

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    fullTestSuite = unittest.TestSuite()
    fullTestSuite.addTest(unittest.makeSuite(TestCard))
    fullTestSuite.addTest(unittest.makeSuite(TestDeck))
    fullTestSuite.addTest(unittest.makeSuite(BlackJackTestCase))
    return fullTestSuite

mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)
