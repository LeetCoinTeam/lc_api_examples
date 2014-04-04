

class Award():
    """ a leetcoin award """
    def __init__(self, playerKey,  playerName, amount, title):
        self.playerKey = playerKey
        self.playerName = playerName
        self.amount = amount
        self.title = title
    def to_dict(self):
        return ({
            u'playerKey': self.playerKey,
            u'playerName': self.playerName,
            u'amount': self.amount,
            u'title': self.title
        })
