# Calculator

import math
import time

print("\nWelcome to my Calculator Program!")
print("\nPlease select one of the options below:\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Quit (Q)")

option = input("\nWhat would you like me to do (1-5)? ").lower()

if option == "1" or option == "addition":
    choice = int(input("\nPlease enter how many numbers you want to add: "))

    total = 0
    for i in range(1, choice + 1):
        number = float((input(f"\nEnter number {i}: ")))
        total += number

    print(f"\nThe total is {total}.\n")

elif option == "2" or option == "subtraction":
    choice = int(input("\nPlease enter how many numbers you want to subtract: "))

    total = 0
    for i in range(1, choice + 1):
        number = float((input(f"\nEnter number {i}: ")))
        total -= number

    print(f"\nThe total is {total}.\n") 

elif option == "3" or option == "multiplication":
    choice = int(input("\nPlease enter how many numbers you want to multiply: "))

    total = 1
    for i in range(1, choice + 1):
        number = float((input(f"\nEnter number {i}: ")))
        total *= number

    print(f"\nThe total is {total}.\n")

elif option == "4" or option == "division":
    print("\nDivison can only be done between two numbers: ")
    number1 = float(input("\nPlease enter number 1: "))
    number2 = float(input("\nPlease enter number 2: "))

    print(f"\nThe total is {number1 / number2}.\n")

elif option == "5" or option == "square root":
    square_root = float(input("\nPlease enter a number: "))
    total = math.sqrt(square_root)
    print(f"\nThe square root of {square_root} is {total}.\n")

elif option == "6" or option == "q" or option == "quit":
    print("\nThe program will end in:")
    print("\n3...")
    time.sleep(1)
    print("\n2...")
    time.sleep(1)
    print("\n1...")
    time.sleep(1)    
    print("\nThanks for using my calculator! Goodbye!\n")
    quit()

else:
    print("\nPlease select a valid option next time, this program will end in:")
    print("\n3...")
    time.sleep(1)
    print("\n2...")
    time.sleep(1)
    print("\n1...")
    time.sleep(1)    
    print("\nThanks for using my calculator! Goodbye!\n")
    quit()
