#Functions for the devour all card game
#Python 3.6.5
#Windows 10

from deck_module import deck
from hand_module import hand
from human_move_module import human_move2
import random


#Level two game functions
def level_2(table, player1, player2, player3, player4):
    """Level 2 game play."""
    while table.size() != 52:
        if not player1.is_empty():
            human_move2(table, player1)
        if not player2.is_empty():
            comp_turn2(table, player2)
        if not player3.is_empty():
            comp_turn2(table, player3)
        if not player4.is_empty():
            comp_turn2(table, player4)

def comp_turn2(table, player2):
    """Computer turn to move."""
    """Computer picks a card at random from hand."""
    """If card is the same as the top on table, player picks card at position 0."""
    import random

    table_card = table.card()
    found = False
    card = 0
    player_card = player2.card_pos(card)
    if player2.size() >= 2:
        card = random.randrange(0, player2.size() - 1)
        player_card = player2.card_pos(card)
        if not table.is_empty():
            if player_card[-1] == table_card[-1]:
                player_card = player2.card_pos(0)
                
    print(table.name, ":\t", table)
    print(player2.name, ":\t", player2)
    print()
    
    
    if not table.is_empty():
        if player_card[-1] == table_card[-1]:
            print()
            print(player2.name, "played", player_card, " and it has same suit as", table_card, "and wil devour all.")
            for i in range(len(table.cards)):
                table.give(table.cards[0], player2)
            input("Press enter to continue:")
        else:
            player2.give(player2.cards[card], table)
    else:
        player2.give(player2.cards[card], table)
        
    print(table.name, ":\t", table)
    print(player2.name, ":\t", player2)
    print()
