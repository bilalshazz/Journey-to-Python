# ATM Simulator

def ATM():

    while True:
        balance_str = input("\nPlease enter your starting balance: £")
        if balance_str.replace('.', '', 1).isdigit():
            balance = float(balance_str)
            break
        else:
            print("\nInvalid input! Please enter a valid number.")

    attempts = 0

    choose_PIN = input("\nPlease enter your PIN: ")
    while not choose_PIN.isdigit():
        print("\nInvalid input! Please enter numbers only: ")
        choose_PIN = input("\nPlease enter your PIN: ")

    while attempts < 3:
        PIN = input("\nPlease enter the PIN again to be able to access your account: ")
        if not PIN.isdigit():
            print("\nInvalid input! Please enter numbers only.")
            continue

        if PIN == choose_PIN:
            print("\nPIN Accepted!")
            break

        else: 
            attempts += 1
            print(f"\nIncorrect PIN. Attempts left: {3 - attempts}.")
    else:
        print("\nToo many incorrect attempts. Please try again later.")
        return

    while True:
        print("\n----- ATM MENU ----- \n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("\nPlease select an option (1-4): ")

        if choice == "1":
            print(f"\nYour current balance is: £{balance:,.2f}\n")

        elif choice == "2":
            amount_str = input("\nEnter amount to deposit: £")
            if not amount_str.replace('.', '', 1).isdigit():
                print("\nInvalid amount!\n")
                continue

            amount = float(amount_str)
            if amount > 0:
                balance += amount
                print(f"\nDeposit successful! New balance: £{balance:,.2f}\n")
            else:
                print("\nInvalid amount.\n")

        elif choice == "3":
            amount_str = input("\nEnter amount to withdraw: £")
            if not amount_str.replace('.', '', 1).isdigit():
                print("\nInvalid amount!\n")
                continue

            amount = float(amount_str)
            if amount > balance:
                print("\nInsufficient funds!\n")
            elif amount <= 0:
                print("\nInvalid amount.\n")
            else:
                balance -= amount
                print(f"\nWithdrawal successful! New balance: £{balance:,.2f}\n")

        elif choice == "4":
            print("\nThank you for using Python ATM Simulator. Goodbye!\n")
            break

        else:
            print("\nInvalid selection. Please choose option 1-4.\n")

ATM()

