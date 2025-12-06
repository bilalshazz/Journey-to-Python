# Random Password Generator

import random 
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
special = string.punctuation

while True:
    try:
        print("\nPassword must be at least 8 characters long.")
        password_length = int(input("\nPlease enter the desired password length (MIN 8): "))
        if password_length < 8:
            print("\nPassword must be at least 8 characters long!")
            continue
        break
    except ValueError:
        print("\nPlease enter a valid number!")

password = [
    random.choice(upper),
    random.choice(lower),
    random.choice(digits),
    random.choice(special)
]

all_chars = upper + lower + digits + special
password += [random.choice(all_chars) for _ in range(password_length - 4)]

random.shuffle(password)
password = ''.join(password)

print(f"\nHere is a strong random password: {password}\n")

