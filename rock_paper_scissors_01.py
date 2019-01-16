print('''
 * * * * * * * * * * * * * * * * * * * * * * * * * * *
 *    Welcome to Rock-Paper-Scissors (Version 1.0)   *
 * * * * * * * * * * * * * * * * * * * * * * * * * * *
''')
print('''\
             # # # # # # # # # # # # # # #
             #   We need two players.    #
             # # # # # # # # # # # # # # #
''')
player_1_name = input("Player 1, enter your name: ")
if player_1_name:
    player_1 = input(f"\n{player_1_name}, enter your choice: ")
    if player_1 == "rock" or player_1 == "paper" or player_1 == "scissors":
        print("\n           = = = No cheating = = =           \n" * 11)
        player_2_name = input("Player 2, enter your name: ")
        if player_2_name:
            player_2 = input(f"\n{player_2_name}, enter your choice: ")
            if player_2 == "rock" or player_2 == "paper" or player_2 == "scissors":
                print("\n   ----   SHOOT!   ----   \n")
                if player_1 == "rock":
                    if player_2 == "rock":
                        print(f"{player_1_name} and {player_2_name} both played {player_1}. "
                              f"The game is tied. Replay!\n")
                    elif player_2 == "paper":
                        print(f"{player_1_name} played {player_1} and {player_2_name} played {player_2}. "
                              f"Paper covers rock. {player_2_name} won!\n")
                    else:
                        print(f"{player_1_name} played {player_1} and {player_2_name} played {player_2}. "
                              f"Rock crushes scissors. {player_1_name} won!\n")
                elif player_1 == "paper":
                    if player_2 == "rock":
                        print(f"{player_1_name} played {player_1} and {player_2_name} played {player_2}. "
                              f"Paper covers rock. {player_1_name} won!\n")
                    elif player_2 == "paper":
                        print(f"{player_1_name} and {player_2_name} both played {player_1}. "
                              f"The game is tied. Replay!\n")
                    else:
                        print(f"{player_1_name} played {player_1} and {player_2_name} played {player_2}. "
                              f"Scissors cuts paper. {player_2_name} won!\n")
                else:   # player_1 == "scissors"
                    if player_2 == "rock":
                        print(f"{player_1_name} played {player_1} and {player_2_name} played {player_2}. "
                              f"Rock crushes scissors. {player_2_name} won!\n")
                    elif player_2 == "paper":
                        print(f"{player_1_name} played {player_1} and {player_2_name} played {player_2}. "
                              f"Scissors cuts paper. {player_1_name} won!\n")
                    else:
                        print(f"{player_1_name} and {player_2_name} both played {player_1}. "
                              f"The game is tied. Replay!\n")
            else:
                print(f'''
                     +-------------------------------------------------------------------+
                        Hey, {player_2_name}.                                            
                        You only have three choices to enter:                            
                        \"rock\", \"paper\" and \"scissors\", which are all in lowercase.
                        Other choices are not allowed.                               
                     +-------------------------------------------------------------------+
                     ''')
        else:
            print('''
                 +-----------------------------------------------------------------------+
                    Sorry, your name is empty. Restart the program and enter your name.
                 +-----------------------------------------------------------------------+
                 ''')
    else:
        print(f'''
             +-------------------------------------------------------------------+
                Hey, {player_1_name}.                                            
                You only have three choices to enter:                            
                \"rock\", \"paper\" and \"scissors\", which are all in lowercase.
                Other choices are not allowed.                               
             +-------------------------------------------------------------------+
              ''')
else:
    print('''
         +-----------------------------------------------------------------------+
            Sorry, your name is empty. Restart the program and enter your name.
         +-----------------------------------------------------------------------+
         ''')
