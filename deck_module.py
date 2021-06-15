#A deck of playing cards
#python 3.6.5

from hand_module import hand
from card_module import card

class deck(hand):
    """A deck of playing cards."""

    def populate(self):
        for suit in card.SUITS:
            for rank in card.RANKS:
                self.add(card(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.cards)





