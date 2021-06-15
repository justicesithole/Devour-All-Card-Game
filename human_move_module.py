#Functions for the devour all card game
#Python 3.6.5
#Windows 10

from deck_module import deck
from hand_module import hand
import random

#Human move function on the second round of the game
def human_move2(table, player1):
    """Second round human move."""
    pos = player1.size() 
    print(player1.name, ":\t", player1)
    print()
    print(player1.name, "please pick a card position between 1 and", pos)
    card = int(input("Take a pick please: "))
    print()
    player_card = player1.card_pos(card)
    
    table_card = table.card()
    print(table.name, ":\t", table)
    print(player1.name, ":\t", player1)
    print()
    if not table.is_empty():
        if player_card[-1] == table_card[-1]:
            print()
            print(player1.name, "played", player_card, " and it has same suit as", table_card, "and will devour all.")
            print()
            for i in range(len(table.cards)):
                table.give(table.cards[0], player1)
        else:
            player1.give(player1.cards[card], table)
    else:
        player1.give(player1.cards[card], table)
    
    print(table.name, ":\t", table)
    print(player1.name, ":\t", player1)
    print()

    return table_card
