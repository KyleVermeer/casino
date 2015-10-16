import random
from card import PlayingCard, Suit, Rank

class Deck:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return str(self.cards)

    def drawCard(self):
        ''' Draw one card from deck. '''
        return self.cards.pop()

    def shuffle(self):
        ''' Shuffles cards in deck. '''
        random.shuffle(self.cards)

    def hasCards(self):
        ''' Returns true if deck has cards remaining, otherwise
            returns false. '''
        if self.cards:
            return True
        else:
            return False

class FiftyTwoCardDeck(Deck):
    ''' Standard 52 card deck. '''

    def __init__(self):
        super().__init__()
        self.resetDeck()

    def resetDeck(self):
        ''' Returns deck to its starting state, containing all cards. '''
        self.cards = []
        for currentSuit in list(Suit):
            for currentRank in list(Rank):
                self.cards.append(PlayingCard(currentRank, currentSuit))

curDeck = FiftyTwoCardDeck()
curDeck.shuffle()
