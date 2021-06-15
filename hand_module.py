#A hand of playing cards module
#A player

class hand(object):
    """A hand of playing cards./ A player"""

    def __init__(self, name = None):
        self.cards = []
        self.name = name

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def name(self):
        return str(self.name)

    def is_empty(self):
        return self.cards == []

    def throw_down(self, card_pos, table):
        self.cards.remove(card)
        table.add(card)

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def size(self):
        return len(self.cards)

    def card(self):
        rep = ""
        if self.cards:
            rep = str(self.cards[-1])
        return rep

    def card_pos(self, pos):
        rep = ""
        if self.cards:
            rep = str(self.cards[pos])
        return rep
