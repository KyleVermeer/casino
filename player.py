class Player:

    def __init__(self, userId):
        self.userId = userId
        self.isDealer = False;

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Player " + self.userId

    def getUserId(self):
        return self.userId

    def isDealer(self):
        return self.isDealer;

    def setDealer(self, isDealer):
        self.isDealer = isDealer
