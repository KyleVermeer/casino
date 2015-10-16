class Player:

    def __init__(self, userId):
        self.userId = userId

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Player " + self.userId

    def getUserId(self):
        return self.userId
