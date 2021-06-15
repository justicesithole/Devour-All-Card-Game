#Functions for the devour all card game
#Python 3.6.5
#Windows 10

from deck_module import deck
from hand_module import hand
import random

#First round of play
def instructions():
    """Instructions for the card game."""
    print(
        """
        Hello and welcome to the 'Devour All Card Game'.
        'Devour All' is a game played by a minimum of 2 to 5 players.
        The game consists of two rounds of playing.
        In the first round each player picks a random card
        from a deck and throws it on the table. If the card
        thrown on the table is the same suit as the card on top
        of the table, for example, if they are both hearts, clubs,
        diamond or spades, the player is forced to devour all the
        cards on the table. The process will continue untill
        all the cards in the deck are finished. If any player
        does not have any cards in hand, then they will be
        declared as a winner.
        In the second round, if any players have cards in hand, then
        they will continue playing with the cards in their hands.
        Each player should pick a card from his/her hand and
        throw it on the table. If the card thrown on table
        is the same as the card on top of the table, then the
        player is forced to devour all the cards on the table.
        The game will continue until only one player is left
        with cards in hand. Then that player will be declared
        the loser. Hope you enjoy playing.
        """
        )

def game_level():
    print()
    level = int(input("Please pick game level between 1 and 6: "))
    while level not in range(1, 7):
        level = int(input("Please pick game level between 1 and 6: "))
    print("Weldone, you will play 'Devour All' level", level)
    print("Prepare yourself human.")
    print()

    return level

        
    
def create_players():
    """Creating players for the game."""
    table = hand("Table")
    deck1 = deck("Deck")
    name = input("Name please: ")
    print()
    player1 = hand(name)
    player2 = hand("Nelson")
    player3 = hand("David")
    player4 = hand("Sam")   
    return table, deck1, player1, player2, player3, player4

def display(table, deck1, player1, player2, player3, player4):
    deck1.populate()
    print()
    print("Deck before shuffling the cards.")
    print(deck1.name, "\t", deck1)
    deck1.shuffle()
    print()
    print("Deck after shuffling the cards.")
    print(deck1.name, "\t", deck1)
    print()
    print("Cards will be picked from the deck and thrown on the table.")
    print()
    print("Players:")
    print("\t1)", player1.name)
    print("\t2)", player2.name)
    print("\t3)", player3.name)
    print("\t4)", player4.name)
    print()
    print("You will play as", player1.name)
    

def human_move1(table, deck1, player1):
    """Human turn to move."""
    pos = deck1.size()
    print()
    print(player1.name, "please pick a card position between 1 and", pos)
    card = int(input("Take a pick please: "))
    print()
    print(player1.name, "you picked a card at position", card)
    deck1.give(deck1.cards[card], player1)
    player_card = player1.card()
    
    table_card = table.card()
   
    if not table.is_empty():
        if player_card[-1] == table_card[-1]:
            print()
            print(player1.name, "picked", player_card, " and it has same suit as", table_card, "and will devour all.")
            print()
            for i in range(len(table.cards)):
                table.give(table.cards[0], player1)
        else:
            player1.give(player1.cards[0], table)
    else:
            player1.give(player1.cards[0], table)
    print(deck1.name, ":\t", deck1)
    print()
    print(table.name, ":\t", table)
    print(player1.name, ":\t", player1)
    print()

def move1(table, deck1, player1, player2, player3, player4):
    """A Player's move."""
    human_move1(table, deck1, player1)
    turn(table, deck1, player2)
    turn(table, deck1, player3)
    turn(table, deck1, player4)
    
def turn(table, deck1, player):
    """A computer's turn."""
    pos = deck1.size()
    print(pos, "cards left.")
    print()
    move(table, deck1, player, pos)
    print(deck1.name, ":\t", deck1)
    print()
    print(table.name, ":\t", table)
    print(player.name, ":\t", player)
    print()
    
def move(table, deck1, player, pos):
    """Each move done by the computer."""
    card = random.randrange(0, pos)
    print("Player picking card at position", card)
    deck1.give(deck1.cards[card], player)
    player_card = player.card()
    
    table_card = table.card()
   
    if not table.is_empty():
        if player_card[-1] == table_card[-1]:
            print()
            print(player.name, "picked", player_card, " and it has same suit as", table_card, "and will devour all.")
            print()
            for i in range(len(table.cards)):
                table.give(table.cards[0], player)
        else:
            player.give(player.cards[0], table)
    else:
            player.give(player.cards[0], table)
