#Functions for the devour all card game
#Python 3.6.5
#Windows 10

from deck_module import deck
from hand_module import hand
from human_move_module import human_move2
import random

#Level four game functions
def level_4(table, player1, player2, player3, player4):
    """Level 4 gameplay."""
    #prev_card = None
    while table.size() != 52:
        if not player1.is_empty():
            human_move2(table, player1)
        if not player2.is_empty():
            comp_turn4(table, player2)
        if not player3.is_empty():
            comp_turn4(table, player3)
        if not player4.is_empty():
            comp_turn4(table, player4)

def comp_turn4(table, player2):
    """Computer turn to move."""
    """Computer picks a card at random, checks if the card is the same suit as table top card."""
    """If the cards suit are the same, checks hand for a different card not the same suit as table top card."""
    
    import random

    table_card = table.card()
    found = False
    card = 0
    count = 0
    max_pos = player2.size() 
    player_card = player2.card_pos(card)
    if player2.size() >= 2:
        card = random.randrange(0, player2.size() - 1)
        player_card = player2.card_pos(card)
        if not table.is_empty():
            if player_card[-1] == table_card[-1]:
                while count != max_pos and not found:
                    player_card = player2.card_pos(count)
                    if player_card[-1] != table_card[-1]:
                        found = True
                    count += 1
        
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
    
