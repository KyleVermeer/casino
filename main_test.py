import unittest
from test.card_test import TestCard
from test.deck_test import TestDeck

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    fullTestSuite = unittest.TestSuite()
    fullTestSuite.addTest(unittest.makeSuite(TestCard))
    fullTestSuite.addTest(unittest.makeSuite(TestDeck))
    return fullTestSuite

mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)
