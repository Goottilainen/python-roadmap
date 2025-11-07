import random

print()
print("*** Guess Number Game ***")
print()
print(" --- IM THINKING IN A NUMBER BETWEEN 1-10... CAN YOU GUESS?")
print()

secret_number = random.randint(1,10)
tries = 0

while True:
    user_number = int(input("Write a number: "))
    tries += 1

    if user_number < secret_number:
        print("Too low!")

    elif user_number > secret_number:
        print("Too high!")

    else:
        print(f"Correct! The secret number was {secret_number}")
        print(f"Number of tries {tries} tries.")
        break
