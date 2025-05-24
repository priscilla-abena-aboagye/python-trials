'''
def validates_user_input():
    user_age = input("Enter your age: ")
    if user_age.isdigit():
        user_age = int(user_age)
        if user_age >= 18:
            print("You are eligible to vote")
        elif user_age < 18:
            print("You are not eligible to vote")
    else: 
        print("Invalid input. Please enter a number")

validates_user_input() 

## Q1 
def favourite_animal():
    fav_ani = input("Enter your favourite animal: ")
    if fav_ani.isdigit():
        print("Please enter an animal")
        input("Enter your favourite animal: ")
    else:
        print("I like too!")
favourite_animal()

## Q2
def product_of_two_num():
    first_num = int(input("Enter the first num: "))
    second_num = int(input("Enter the second num: "))
    product = first_num * second_num
    print(f"The product of the numbers are {product}")
product_of_two_num()



# Q3
def checks_the_sign():
    user_input = int(input("Enter your number: "))
    if user_input == 0:
        print("Zero")
    elif user_input > 0:
        print("Positive")
    else:
        print("Negative")
checks_the_sign()

# Q4
def characters_of_name():
    user_name = input("Enter your name: ")
    num_of_char = 0
    for char in user_name:
        num_of_char += 1
    print(num_of_char)
characters_of_name()

# Q5, Q6
def list_colours():
    colours = ["red", "yellow", "blue"] 
    second_colour = colours[1]
    print(second_colour)
    colours.append("purple")
    print(colours)
list_colours() 

# Q7
def prints_items():
    fruits = ["mango", "banana", "orange"]
    for fruit in fruits:
        print(fruit)
prints_items()
'''
# Q8
def even_numbers():
    for num in range(2, 11):
        if num % 2 == 0:
            print(num)
even_numbers()

# Q9
def say_hello():
    print("Hello!")
say_hello()

# Q10
def greet_user():
    print("Hi!.")
greet_user()

# Q11
def sum_of_two_numbers():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    sum_of_num = num1 + num2
    print(sum_of_num)
sum_of_two_numbers()