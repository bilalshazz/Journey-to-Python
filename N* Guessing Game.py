# Number Guessing Game

import random

def GuessingGame():

    lives = 5
    number = random.randint(1, 100)

    while True:
        print("\nThe computer has chosen a number between 1 and 100. You have 5 lives. For every wrong guess you lose 1 life.")
        guess = int(input("\nPlease enter your guess (1 - 100): "))

        if guess < 1 or guess > 100:
            print("\nYour guess must be between 1 and 100!")
            continue

        if guess == number:
            print(f"\nWell done! You have guessed the number! You still have {lives} lives.")
            answer = ""
            while answer not in ("yes", "no"):
                answer = input("\nWould you like to play again? (yes/no): ").lower()
                if answer not in ("yes", "no"):
                    print("\nPlease enter a valid answer!")

            if answer == "yes" or answer == "y":
                GuessingGame()
                break
            elif answer == "no" or answer == "n":
                print("\nThanks for playing!")
                break

        else:
            lives -= 1
            print(f"\nIncorrect! You just lost a life. You have {lives} lives left.")

            if lives == 0:
                print(f"\nYou lost! The correct answer was {number}.")
                answer = ""
                while answer not in ("yes", "y", "no", "n"):
                    answer = input("\nWould you like to play again? ").lower()
                    if answer not in ("yes", "y", "no", "n"):
                        print("\nPlease enter a valid answer!")
                if answer == "yes" or answer == "y":
                    GuessingGame()
                else:
                    print("\nThanks for playing!")
                break

            hint = input("\nWould you like me to give you a hint? (yes/no): ").lower()

            if hint == "yes" or hint == "y":
                level = input("\nPlease select the hint level you would like to receive. Level 1 (1): Free (simple hint). Level 2 (2): One life will be deducted from your total, but you will receive a good hint. ")
                if level == "1":
                    if abs(guess - number) <= 5:
                        print("\nHint Level 1: You're VERY close!")
                    elif abs(guess - number) <= 15:
                        print("\nHint Level 1: You're close!")
                    else:
                        print("\nHint Level 1: You're far off!")
                elif level == "2":
                    lives -= 1
                    if 1 <= number <= 25:
                        print("\nHint Level 2: The number is between 1 - 25.")
                    elif 26 <= number <= 50:
                        print("\nHint Level 2: The number is between 26 - 50.")
                    elif 51 <= number <= 75:
                        print("\nHint Level 2: The number is between 51 - 75.")
                    elif 76 <= number <= 100:
                        print("\nHint Level 2: The number is between 76 - 100.")
            elif hint == "no":
                print("\nI like that confidence! No hints will be given. Good Luck!")

GuessingGame()

