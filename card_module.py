#Card class module
#Pyrhon 3.6.5
#On windows 10

class card(object):
    """A playing card"""
    SUITS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
    RANKS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep
