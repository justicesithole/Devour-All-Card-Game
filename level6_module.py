#Functions for the devour all card game
#Python 3.6.5
#Windows 10

from deck_module import deck
from hand_module import hand
from human_move_module import human_move2
import random

#Level six    

def level_6(table, player1, player2, player3, player4):
    """Level 3 gameplay."""
    #prev_card = None
    while table.size() != 52:
        players = players_left(player1, player2, player3, player4)
        if not player1.is_empty():
            human_move2(table, player1)
            
        if not player2.is_empty() and player3.is_empty() and player4.is_empty():
            comp_turn6(table, player2, player1, players)
        elif not player2.is_empty():
            comp_turn6(table, player2, player1, players)
            
        if not player3.is_empty() and player4.is_empty():
            comp_turn6(table, player3, player1, players)
        elif not player3.is_empty():
            comp_turn6(table, player3, player1, players)
            
        if not player4.is_empty():
            comp_turn6(table, player4, player1, players)

def players_left(player1, player2, player3, player4):
    """Checks how many players are left in the game."""
    """For computer to know which card to play inoder to mark the human."""
    count = 0
    if not player1.is_empty():
        count += 1
    if not player2.is_empty():
        count += 1
    if not player3.is_empty():
        count += 1
    if not player4.is_empty():
        count += 1
    return count
    
    
def comp_turn6(table, player2, next_player, players):
    """Second round computer move."""
    """If computer has more cards than human, then computer focuses on playing same suit."""
    """Computer will check if card has the same suit as the top table card."""
    """Target is to mark the human not to win."""
    """If computer cards are less than human, then computer picks a card from most suit list."""
    
    card = 0
    suit = []
    if table.size() >= players and player2.size() > next_player.size():
        card = card_pos2(table, player2, players)
        
        
    if player2.size() >= 2 and card == 0:
        suit = most_suit(table, player2)
        card = card_pos(table, player2, suit)

    if not player2.is_empty():    
        turn6(table, player2, card)

def turn6(table, player2, card):
    """Computer turn to play."""
    print(table.name, ":\t", table)
    print(player2.name, ":\t", player2)
    print()
    table_card = table.card()
    player_card = player2.card_pos(card)
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


def most_suit(table, player):
    """Checking computer hand for the most 2 suits cards."""
    table_card = table.card()
    spade_count = 0
    club_count = 0
    heart_count = 0
    diamond_count = 0
    next_card = None

    #if player.size() >= 2:
    for card in player.cards:
        if "s" in str(card):
            spade_count += 1

        elif "c" in str(card):
            club_count += 1
        elif "h" in str(card):
            heart_count += 1
        elif "d" in str(card):
            diamond_count += 1
        else:
            continue

    suits = [spade_count, club_count, heart_count, diamond_count]
    suits.sort()
    suit = []
    if spade_count == suits[-1]:
        suit.insert(0, "s")
    elif club_count == suits[-1]:
        suit.insert(0, "c")
    elif heart_count == suits[-1]:
        suit.insert(0, "h")
    elif diamond_count == suits[-1]:
        suit.insert(0, "d")

    if spade_count == suits[-2] and "s" not in suit:
        suit.insert(1, "s")
    elif club_count == suits[-2] and "c" not in suit:
        suit.insert(1, "c")
    elif heart_count == suits[-2] and "h" not in suit:
        suit.insert(1, "h")
    elif diamond_count == suits[-2] and "d" not in suit:
        suit.insert(1, "d")

    return suit

def card_pos(table, player, suit):
    
    table_card = table.card()
    count = 0
    counter = 0
    found = False
    founder = False
    print()
    print("suit", suit)
    print()
    while count != player.size() and not found:
        card = player.card_pos(count)
        if suit[0] in card:
            found = True
        else:
            count += 1

    if len(suit) == 2:
        while counter != player.size() and not founder:
            card = player.card_pos(counter)
            if suit[1] in card:
                founder = True
            else:
                counter += 1

    if found and suit[0] not in table_card:
        return count
    elif len(suit) == 2:
        if founder and suit[1] not in table_card:
            return counter
    else:
        return count
    
def card_pos2(table, player, players):
    
    """Return the posiotion of the most suit card."""
    """This function is called only if computer cards are more than human card."""
    """And also if table cards are more than number of players."""
    """Computer takes the position and plays that card."""
    
    found = False
    not_found = False
    count = 0
    table_card1 = table.card()
    table_card = table.card_pos(-players)
    while count != player.size() and not found and not not_found:
        card = player.card_pos(count)
        if card[-1] == table_card[-1]:
            if card[-1] == table_card1[-1]:
                not_found = True
            else:
                found = True
        else:
            count += 1

    if found:
        return count
    else:
        count = 0
        return count
    
