from .deck import *
from .player import *

class BlackJack:

    def __init__(self, players):
        # @TODO: Consider moving to 'table' instead of players
        self.__players = players

        # Initialize a dealer
        dealer = Player(0)
        dealer.setDealer(True)
        self.__players.append(dealer)

        #Intialize a deck
        self.__currentDeck = FiftyTwoCardDeck()
        self.__currentDeck.shuffle()
        self.__currentRound = None

    def playRound(self):
        self.initialDeal()
        for currentPlayer in self.__players:
            self.playHand(currentPlayer)

    def initialDeal(self):
        ''' Provide initial deal to all players. '''
        self.__currentRound = Round(self.__players)
        i = 0
        # deal 2 cards to each player
        while i < 2:
            for currentPlayer in self.__players:
                currentCard = self.__currentDeck.drawCard()
                # Deal with first dealer card facedown
                if i == 0 and currentPlayer.isDealer():
                    currentCard.setFaceDown(True)
                handForPlayer = self.__currentRound.getHandForPlayer(currentPlayer)
                handForPlayer.addCard(currentCard)
            i += 1

    def playHand(self, player):
        ''' Plays the current hand for the given player. '''
        currentHand = self.__currentRound.getHandForPlayer(player)
        while True:
            playerAction = self.__figureOutPlayerAction(player)
            if playerAction is "stay":
                break;
            elif playerAction is "hit":
                newCard = self.__currentDeck.drawCard();
                currentHand.addCard(newCard);
            else:
                print("Unkown Action:", playerAction)

    def __figureOutPlayerAction(self, player):
        currentHand = self.__currentRound.getHandForPlayer(player)
        print("Current Hand: " + str(currentHand) + " - Count: " + str(currentHand.getCount()))
        # Continue to loop until they enter a valid response
        while True:
            response = input('What would you like to do? "hit" (h) or "stay" (s)?\n')
            if response in ["hit","h"]:
                return "hit"
            elif response in ["stay","s"]:
                return "stay"
            else:
                print('\"',response,'\" is not a valid response.')

class Round:

    def __init__(self, players):
        self.__players = players
        self.__playerToHand = {}
        # initialize cards for players map
        for currentPlayer in self.__players:
            self.__playerToHand[currentPlayer.getUserId()] = Hand(currentPlayer)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__playerToHand)

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

#game = BlackJack([Player(1), Player(2)])
#game.playRound()
