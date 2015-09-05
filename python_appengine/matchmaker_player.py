
class MatchmakerPlayer():
    """ a leetcoin matchmaker player """
    def __init__(self, platformID, kills, deaths, name, weapon, rank):
        self.platformID = platformID
        self.kills = kills
        self.deaths = deaths
        self.name = name
        self.rank = rank
        self.weapon = weapon
        
    def to_dict(self):
        return ({
                u'platformID': self.platformID,
                u'kills': self.kills,
                u'deaths': self.deaths,
                u'name': self.name,
                u'rank': self.rank,
                u'weapon': self.weapon
                })