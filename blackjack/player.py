class Player:

    def __init__(self, userId):
        self.__userId = userId
        self.__isDealer = False;

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.__isDealer:
            return "Dealer " + str(self.__userId)
        else:
            return "Player " + str(self.__userId)

    def getUserId(self):
        return self.__userId

    def isDealer(self):
        return self.__isDealer;

    def setDealer(self, isDealer):
        self.__isDealer = isDealer
