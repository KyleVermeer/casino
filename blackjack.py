from deck import *
from player import *

class BlackJack:

    def __init__(self, players):
        # @TODO: Consider moving to 'table' instead of players
        self.players = players

        # Initialize a dealer
        dealer = Player(0)
        dealer.setDealer(True)
        self.players.append(dealer)

        #Intialize a deck
        self.currentDeck = FiftyTwoCardDeck()
        self.currentDeck.shuffle()
        self.currentRound = None

    def playRound(self):
        self.initialDeal()

    def initialDeal(self):
        ''' Provide initial deal to all players. '''
        self.currentRound = Round(self.players)
        i = 0
        # deal 2 cards to each player
        while i < 2:
            for currentPlayer in self.players:
                currentCard = self.currentDeck.drawCard()
                # Deal with first dealer card facedown
                if i == 0 and currentPlayer.isDealer():
                    currentCard.setFaceDown(True)
                handForPlayer = self.currentRound.getHandForPlayer(currentPlayer)
                handForPlayer.addCard(currentCard)
            i += 1

        self.currentRound.printCounts()

    def turnByPlayer(self, player):
        pass;

class Round:

    def __init__(self, players):
        self.players = players
        self.__playerToHand = {}
        # initialize cards for players map
        for currentPlayer in self.players:
            self.__playerToHand[currentPlayer.getUserId()] = Hand(currentPlayer)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.playerToHand)

    def getHandForPlayer(self, player):
        ''' Returns the hand for the givne player. '''
        return self.__playerToHand[player.getUserId()]

    def printCounts(self):
        ''' Prints the count of each hand. '''
        for currentHand in self.__playerToHand.values():
            print(str(currentHand) + " - Count: " + str(currentHand.getCount()))

class Hand:

    def __init__(self, player):
        self.__player = player
        self.__cards = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__cards)

    def addCard(self, card):
        self.__cards.append(card)

    def getCount(self):
        ''' Returns the current count for the hand (sum of all the card values).
            @NOTE (kvermeer): Heavily consider moving this to a strategy class.
            '''
        currentCount = 0
        print(Rank.Two.name)
        for currentCard in self.__cards:
            cardRank = currentCard.getRank()
            # Less than a face card, just count value
            if (cardRank.value <= 10):
                    currentCount += cardRank.value
            else:
                # Count Aces
                if (cardRank == Rank.Ace):
                    currentCount += 11
                # Count Face cards
                else:
                    currentCount += 10
        return currentCount

game = BlackJack([Player(1), Player(2)])
game.initialDeal()
