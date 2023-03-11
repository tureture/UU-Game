import os
import random
from game_loop import game

print("Welcome to the game")
input("Press Enter to proceed")
game_type = ""
# Clear the screen
os.system("cls" if os.name == "nt" else "clear")

# Ask the user for their age
while True:
    try:
        age = input("Please enter your age: ")
        if age == "q":
            print("Exiting the game...")
            exit()
        age = int(age)
        if age >= 4:
            break
        else:
            print("Sorry, you must be at least 4 years old to play this game.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Display the game modes
print("Game Modes:")
print("1. 1 vs 1 Mode")
print("2. Tournament Mode")

# Ask the user to select a game mode
while True:
    mode = input("Enter your choice (1-2) or 'q' to quit: ")
    if mode == "1":
        print("You have selected 1 vs 1 Mode.")
        break
    elif mode == "2":
        print("You have selected Tournament Mode.")
        break
    elif mode == "q":
        print("Exiting the game...")
        exit()
    else:
        print("Invalid option. Please try again.")

# Ask the user to select the type of game in 1 vs 1 mode
if mode == "1":
    while True:
        game_type = input(
            "1 vs 1 Mode: Select game type (1-3)\n1. Human vs Human\n2. Human vs AI\n3. AI vs AI\nor 'q' to quit\nEnter your choice (1-3): ")
        if game_type == "1":
            print("You have selected Human vs Human.")
            break
        elif game_type == "2":
            print("You have selected Human vs AI.")
            break
        elif game_type == "3":
            print("You have selected AI vs AI.")
            break
        elif mode == "q":
            print("Exiting the game...")
            exit()
        else:
            print("Invalid option. Please try again.")
else:
    while True:
        total_players = input(
            "Enter total players in a tournament (Max 8 players can play and greater than 2)\nor 'q' to quit\n ")
        if total_players == "q":
            print("Exiting the game...")
            exit()
        total_players = int(total_players)
        if total_players > 8 or total_players < 2:
            print("Total players must be between 2 and 8.")
            continue
        else:
            break

    colors = ["white", "black"]
    player_list = []
    for i in range(1, total_players + 1):
        player_name = input(f"Enter name for Player {i}: ")
        player_list.append((player_name, random.choice(colors)))

    rounds = total_players - 1
    match_count = 0
    players_copy = player_list.copy()
    round_matches_list = []
    for round_num in range(rounds):
        print(f"\nRound {round_num + 1}:")
        round_matches = []
        for i in range(total_players // 2):
            p1, p2 = random.sample(players_copy, 2)
            round_matches.append((p1, p2))
            players_copy.remove(p1)
            players_copy.remove(p2)
        for match in round_matches:
            match_count += 1
            print(f"Match {match_count}: {match[0][0]}  vs {match[1][0]} ")
            round_matches_list.append((match[0][0], match[1][0], ""))
        players_copy = player_list.copy()

    current_match = 0
    last_game_color = ""
    while True:
        match = round_matches_list[current_match]
        if last_game_color == match[0][1]:
            player1_color = "white" if last_game_color == "black" else "black"
        else:
            player1_color = random.choice(colors)
        player2_color = "white" if player1_color == "black" else "black"
        print(f"\nMatch {current_match + 1}: {match[0]} ({player1_color}) vs {match[1]}({player2_color})")

        while True:
            # Input our code here somehow
            if player1_color == "white":
                curr_game = game(match[1], match[0])
            else:
                curr_game = game(match[0], match[1])
            curr_game.start()

            
            if curr_game.winner is None:
                if current_match == len(round_matches_list) - 1:

                    print("All matches finished.")
                    exit()
                print(f"Next match: {round_matches_list[current_match + 1]}")
                break

            elif curr_game.winner == match[0] or curr_game.winner == match[1]:
                round_matches_list[current_match] = (match[0], match[1], "Finished")
                last_game_color = player1_color
                current_match += 1
                break

            elif current_match == len(round_matches_list) - 1:
                print("All matches finished.")
                exit()


# Ask for player names in Human vs Human game type

if game_type == "1":
    print("Enter the player names or enter 'q' to exit from the game. ")
    player1_name = input("Enter name of Player 1: ")
    player2_name = input("Enter name of Player 2: ")
    if player1_name == "q" or player2_name == "q":
        print("Exiting the game...")
        exit()
    while player1_name == player2_name:
        print("Both players can't have same name.Try Again")
        player2_name = input("Enter name of Player 2: ")
    # Ask for player colors
    while True:
        player1_color = input(f"{player1_name}, select your color (Black or White) or enter 'q' to exit from the game.: ")
        if player1_color == "q":
            print("Exiting the game...")
            exit()
        elif player1_color.lower() == "black":
            break
        elif player1_color.lower() == "white":
            break
        else:
            print("Invalid input. Please try again.")

    while True:
        player2_color = input(f"{player2_name}, select your color (Black or White) or enter 'q' to exit from the game: ")
        if player1_color == "q":
            print("Exiting the game...")
            exit()
        elif player2_color.lower() == "black":
            break
        elif player2_color.lower() == "white":
            break
        else:
            print("Invalid input. Please try again.")

    print(f"{player1_name} has selected {player1_color} and {player2_name} has selected {player2_color}.")

    # Ask for player turn this does not apply for our game
    """ while True:
        player_turn = input(f"{player1_name} : If you want first turn then enter 1 otherwise 2 or enter 'q' to exit from the game: ")
        if player_turn == "q":
            print("Exiting the game...")
            exit()
        elif player_turn == "1" or player_turn == "2":
            break
        else:
            print("Invalid input! Please enter 1 for first turn or 2 for second turn.")

    if player_turn == "1":
        print(f"{player1_name} will play first.")
    else:
        print(f"{player2_name} will play first.") """

if game_type == "2" or game_type == "3":
    while True:
        ai_difficulty = input("Select level of difficulty for AI (1- Noob, 2- Intermediate, 3- Pro)  or enter 'q' to exit from the game: : ")
        if ai_difficulty == "q":
            print("Exiting the game...")
            exit()
        elif ai_difficulty == "1" or ai_difficulty == "2" or ai_difficulty == "3":
            break
        else:
            print("Invalid input! Please enter the level of difficulty for AI in the form of 1, 2, or 3.")

    if ai_difficulty == "1":
        print("AI level set to Noob.")
    elif ai_difficulty == "2":
        print("AI level set to Intermediate.")
    else:
        print("AI level set to Pro.")

    print("Enter the player names or enter 'q' to exit from the game. ")
    player1_name = input("Enter name of Player 1: ")
    player2_name = input("Enter name of Player 2: ")
    if player1_name == "q" or player2_name == "q":
        print("Exiting the game...")
        exit()
    while player1_name == player2_name:
        print("Both players can't have same name.Try Again")
        player2_name = input("Enter name of Player 2: ")

    while True:
        player1_color = input("Player 1: Choose your color (Black or White) or enter 'q' to exit from the game. : ").lower()
        if player1_color == "q":
            print("Exiting the game...")
            exit()
        elif player1_color == "black" or player1_color == "white":
            break
        else:
            print("Invalid input! Please choose either Black or White.")

    while True:
        player2_color = input("Player 2: Choose your color (Black or White) or enter 'q' to exit from the game: ").lower()
        if player2_color == "q":
            print("Exiting the game...")
            exit()
        elif player2_color == "black" or player2_color == "white":
            if player2_color != player1_color:
                break
            else:
                print("Both players can't have the same color. Please choose a different color.")
        else:
            print("Invalid input! Please choose either Black or White.")

    """ while True:
        player_turn = input(f"{player1_name} : If you want first turn then enter 1 otherwise 2 or enter 'q' to exit from the game. : ")
        if player_turn == "q":
            print("Exiting the game...")
            exit()
        elif player_turn == "1" or player_turn == "2":
            break
        else:
            print("Invalid input! Please enter 1 for first turn or 2 for second turn.")

    if player_turn == "1":
        print(f"{player1_name} will play first.")
    else:
        print(f"{player2_name} will play first.") """