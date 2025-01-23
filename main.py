import random

lowest_number = 1
highest_number = 50
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Welcome to the Python Guessing game")
print("------------------------------------")
print(f"Select a number between {lowest_number} and {highest_number}")
print("------------------------------------")


while is_running:
    guess = input("Select your number: ")

    if not guess.isdigit():
        print("Invalid")
        print(f"Please select a number between {lowest_number} and {highest_number}")
    else: 
        pass


# print(answer)

