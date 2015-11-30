import random
from .card import PlayingCard, Suit, Rank

class Deck:

    def __init__(self):
        self._cards = []

    def __str__(self):
        return str(self._cards)

    def drawCard(self):
        ''' Draw one card from deck. '''
        return self._cards.pop()

    def shuffle(self):
        ''' Shuffles cards in deck. '''
        random.shuffle(self._cards)

    def hasCards(self):
        ''' Returns true if deck has cards remaining, otherwise
            returns false. '''
        if self._cards:
            return True
        else:
            return False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self._cards)

class FiftyTwoCardDeck(Deck):
    ''' Standard 52 card deck. '''

    def __init__(self):
        super().__init__()
        self.resetDeck()

    def resetDeck(self):
        ''' Returns deck to its starting state, containing all cards. '''
        self._cards = []
        for currentSuit in list(Suit):
            for currentRank in list(Rank):
                self._cards.append(PlayingCard(currentRank, currentSuit))
