from deck import *
from player import *

class BlackJack:

    def __init__(self, players):
        # @TODO: Consider moving to 'table' instead of players
        self.players = players
        dealer = Player(0)
        dealer.setDealer = True
        self.players.append(dealer)
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
                self.currentRound.giveCardToPlayer(currentCard, currentPlayer)
            i += 1
        print(self.currentRound)

    def turnByPlayer(self, player):
        pass;

class Round:

    def __init__(self, players):
        self.players = players
        self.playerToCards = {}
        # initialize cards for players map
        for currentPlayer in self.players:
            self.playerToCards[currentPlayer.getUserId()] = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.playerToCards)

    def giveCardToPlayer(self, card, player):
        ''' Give card to player. '''
        self.playerToCards[player.getUserId()].append(card)

class PlayerCards:

    def __init__(self, player):
        this.player = player
        this.cards = []

    def addCard(self, card):
        this.cards.append(card)

game = BlackJack([Player(1), Player(2)])
game.initialDeal()
