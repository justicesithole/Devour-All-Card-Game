#Functions for the devour all card game
#Python 3.6.5
#Windows 10

from level1_module import level_1
from level2_module import level_2
from level3_module import level_3
from level4_module import level_4
from level5_module import level_5
from level6_module import level_6

from round1_module import instructions, create_players, display, game_level, move1

def main():
    instructions()
    print()
    table, deck1, player1, player2, player3, player4 = create_players()
    display(table, deck1, player1, player2, player3, player4)
    level = game_level()

    while not deck1.is_empty():
        move1(table, deck1, player1, player2, player3, player4)

    print()
    print(player1.name, "has", player1.size(), "cards")
    print(player2.name, "has", player2.size(), "cards")
    print(player3.name, "has", player3.size(), "cards")
    print(player4.name, "has", player4.size(), "cards")


    #Level 1
    if level == 1:
        level_1(table, player1, player2, player3, player4)
            
    #Level 2
    elif level == 2:
        level_2(table, player1, player2, player3, player4)

    #level 3
    elif level == 3:
        level_3(table, player1, player2, player3, player4)
        
    #Level 4
    elif level == 4:
        level_4(table, player1, player2, player3, player4)

    #Level 5
    elif level == 5:
        level_5(table, player1, player2, player3, player4)

    #Level 6
    else:
        level_6(table, player1, player2, player3, player4)


main()
print("GAME OVER")
input("Press enter to exit:")

