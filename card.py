from enum import Enum, unique

class PlayingCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.rank.name + " of " + self.suit.name + "s"

    def getRank(self):
        ''' Returns rank of card. '''
        return self.rank

    def getSuit(self):
        ''' Returns suit of card. '''
        return self.suit

@unique
class Suit(Enum):
    Heart = 1
    Club = 2
    Diamond = 3
    Spade = 4

@unique
class Rank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14
