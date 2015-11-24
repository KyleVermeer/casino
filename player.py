class Player:

    def __init__(self, userId):
        self.userId = userId
        self.__isDealer = False;

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.__isDealer:
            return "Dealer " + str(self.userId)
        else:
            return "Player " + str(self.userId)

    def getUserId(self):
        return self.userId

    def isDealer(self):
        return self.__isDealer;

    def setDealer(self, isDealer):
        self.__isDealer = isDealer
