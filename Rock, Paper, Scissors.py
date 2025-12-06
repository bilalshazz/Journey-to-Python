# Welcome to my RPS game.

import random

user_choices = ["R", "P", "S", "1"]
computer_choices = ["R", "P", "S"]
user_score = 0
computer_score = 0
rounds = 0

username = input("\nPlease enter your name: ").capitalize()
scoring_system = print(f"\nHi {username}. Here is the scoring system: A win gives you 3 points, A draw gives you 1 point, and a loss gives you 0 points.")

def RPSgame():
    global user_score, computer_score
    while True:
        user_input = input("\nPlease enter 'R' (rock), 'P' (paper), 'S' (scissors), or '1' to check the Score: ").upper()
        if user_input not in user_choices:
            print("\nInvalid choice!")
            continue
        elif user_input == "1":
            print(f"\nThe current score is: {username} = {user_score} | Computer = {computer_score}.")
            continue_game = input("\nDo you want to keep playing? (Y/N): ").upper()
            if continue_game == "Y" or continue_game == "YES":
                continue
            elif continue_game == "N" or continue_game == "NO":
                break
            else:
                print("\nInvalid Option!")
                print(continue_game)
                continue

        computer_plays = random.choice(computer_choices)

        if user_input == computer_plays:
            print(f"\nThat's a draw. You played {user_input} and the computer played {computer_plays}.")
            user_score += 1
            computer_score += 1

        elif user_input == "R" and computer_plays == "P":
            print(f"\nYou lost! You played '{user_input}/Rock' and the computer played '{computer_plays}/Paper'.")
            user_score += 0
            computer_score += 3

        elif user_input == "P" and computer_plays == "R":
            print(f"\nYou won! You played '{user_input}/Paper' and the computer played '{computer_plays}/Rock'.")
            user_score += 3
            computer_score += 0

        elif user_input == "P" and computer_plays == "S":
            print(f"\nYou lost! You played '{user_input}/Paper' and the computer played '{computer_plays}/Scissors'.")
            user_score += 0
            computer_score += 3

        elif user_input == "S" and computer_plays == "P":
            print(f"\nYou won! You played '{user_input}/Scissors' and the computer played '{computer_plays}/Paper'.")
            user_score += 3
            computer_score += 0

        elif user_input == "R" and computer_plays == "S":
            print(f"\nYou won! You played '{user_input}/Rock' and the computer played '{computer_plays}/Scissors'.")
            user_score += 3
            computer_score += 0

        elif user_input == "S" and computer_plays == "R":
            print(f"\nYou lost! You played '{user_input}/Scissors' and the computer played '{computer_plays}/Rock'.")
            user_score += 0
            computer_score += 3

RPSgame()

