import random

lowest_number = 1
highest_number = 50
answer = random.randint(lowest_number, highest_number)
print("python's answer = ", answer)
guesses = 0
is_running = True

print("Welcome to the Python Guessing game")
print("------------------------------------")
print(f"Select a number between {lowest_number} and {highest_number}")
print("------------------------------------")


while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("The number is out of range")
            print(f"Please select a number between {lowest_number} and {highest_number}")
        elif guess > answer:
            print("Too High! Try again")
        elif guess < answer:
            print("Too Low! Try again")
        else:
            print(f"Correct! Tha answer was {answer}")
            print(f"It took {guesses} guesses for you to get the amswer")
            is_running = False
    
    else:
        print("Invalid")
        print(f"Please select a number between {lowest_number} and {highest_number}")



    


# print(answer)

