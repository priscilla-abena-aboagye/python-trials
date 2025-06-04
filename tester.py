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

# Q12
def first_and_last_letters():
    word = "butterfly"
    print(word[0])
    print(word[-1])
first_and_last_letters()

# Q13
def output():
    pets = ["dog", "cat", "fish"] 
    print(pets[-1]) # "fish"
output()

# Q14
def case_convertor():
    language = "python"
    print(language.upper())
case_convertor()

# Q15
def password_validator():
    password = input("Enter your password: ")
    if password == "admin123":
        print("Access granted")
    else:
        print("Access denied")
password_validator()

#Q16
def product_of_numbers():
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))
    product = number1 * number2
    print(product)
product_of_numbers()

#Q17
def favorite_colors():
    colors = ["blue", "green", "brown"]
    print(colors[1])
favorite_colors()

# Q18
def user_bio():
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    print(f"Hi {user_name}, you are {user_age} years old")
user_bio()

#Q19
def square_number():
    user_num = int(input("Enter the number to be squared: "))
    square_num = pow(user_num, 2)
    return square_num
ans = square_number()
print(ans)

# Q20
def prints_python():
    for i in "python":
        print(i, "\n")
prints_python()

# Q21
def prints_even_numbers():
    num = [3, 6, 9, 12, 15]
    for n in range(0, len(num)):
        index_num = num[n]
        if index_num % 2 == 0 :
            print(index_num)
prints_even_numbers()
'''

# Q22
def key_value_pair():
    user_info = {
        "name": "Abena",
        "age": 13,
        "city": "Accra"
    }
    print(user_info["city"])
key_value_pair()

# Q23
def counts_sentences():
    user_sentence = input("Enter a sentence: ")
    word_count = 0
    for word in user_sentence:
        word_count += 1
    print(word_count)
counts_sentences()

# Q24
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
ans = is_even(4)
print(ans)

# Q25
def checks_status():
    number = int(input("Enter your number: "))
    if number == 0:
        print("Zero")
    elif number > 0:
        print("Positive")
    else:
        print("Negative")
checks_status()
