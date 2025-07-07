# Improving python skills using Bro Code
import math
import time

'''
# Strings
first_name = "Prscilla"
food = "banku"
print(f"Hello my name is {first_name}")
print(f"My favourite food is {food}")

# Integers
age = 20
quantity = 5
num_of_students = 35
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"There are {num_of_students} people in the class")

# float
price = 4.5
gpa = 3.5
distance = 3.6
print(f"The price of the goods are ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} km")

# boolean
is_student = True
for_sale = False
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("This is for sale")
else:
    print("This is NOT for sale")

if is_online:
    print("You are online")
else:
    print("You are NOT online")

# Typecasting
name = "Priscilla"
year = 2025
amount = 3.7
student = True

year_1 = int(year)
year_2 = float(year)
year_3 = str(year)
year_4 = bool(year)

print(year_1, year_2, year_3, year_4)



# Input
user_name = input("What's your name?: ")
user_age = int(input("What is your age?: "))
user_age = user_age + 1
print(f"Hello {user_name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {user_age} years old")


# Calculating for the area of a rectangle

user_length = float(input("Enter the length (cm): "))
user_width = float(input("Enter your width (cm): "))

area = user_length * user_width
print(f"The area of the rectangle is {area}cm^2")

# Shopping cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many will you buy?: "))
amount = price * quantity

print(f"{item} cost ${price}. Purchasing {quantity} will the cost ${amount}")

# Madlibs game
status = input("Is the sun up or down?: ")
mood = input("How are you feeling today?: ")
influence = input("What changes your mood?: ")
status_1 = input(f"How do you feel after {influence}?: ")

print(f"The sun is {status} today. I am really {mood}. I have my {influence} to make me {status_1}.")
print(f"Since I have {influence}, I am sure to be {status_1}")


# Arithmetic
 
x = 3.2
y = 4.55
z = 12

round_num= round(y)
max_num = max(x, y, z)
min_num = min(x, y, z)
exponent = pow(x, 3)
round_up = math.ceil(x)
round_down = math.floor(y)
square_num = math.sqrt(z)
print(round_num, max_num, min_num, exponent)
print(round_up, round_down, square_num)

# Circumference of a circle

user_raduis = float(input("Enter the raduis of the circle(cm): "))

circumference = 2 * (math.pi) * user_raduis
print(f"The circumference of the circle with radius {user_raduis}cm is {round(circumference, 3)}cm")

# Area of a circle

user_area_raduis = float(input("Enter the raduis of the circle(cm): "))
area = (math.pi) * user_area_raduis ** 2
print(f"The area of the circle with raduis {user_area_raduis}cm is {round(area, 3)}cm^2")

# Hypotenus of a triangle

user_adjacent = float(input("Enter the adjacent length(cm): "))
user_opposite = float(input("Enter the opposite lenghth(cm): "))
hypothenus = math.sqrt(pow(user_adjacent, 2) + pow(user_opposite, 2))
print(f"The hypothenus for the triangle with an adjacent of {user_adjacent}cm and an opposite of {user_opposite}cm is {hypothenus}")

# If statement
response = input("Did you drink coffee today (Y/N)?: ")
if response == "Y":
    print("No more coffee for you!")
else: 
    print("You can have only one coffee for the day")

user_name = input("Enter your name: ")
if user_name == "":
    print("You did not enter your name!")
else:
    print(f"Hello {user_name}")

user_age_var = int(input("Enter your age: "))

if  user_age_var >= 18:
    print("You can sign up")
elif user_age_var < 0:
    print("You have not been born yet!")
else:
    print("You must be 18+ to sign up")
    # Python Calulator

user_operator = input("Enter ypur operand (+, -, *, /): ")
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
answer = 0

if user_operator == "+":
    answer = number_1 + number_2
    print(round(answer, 3))
elif user_operator == "-":
    answer = number_1 - number_2
    print(round(answer, 3))
elif user_operator == "*":
    answer = number_1 * number_2
    print(round(answer, 3))
elif user_operator == "/":
    answer = number_1 / number_2
    print(round(answer, 3))
else:
    print(f"{user_operator} is not a valid operaor")

# Weight convertor
weight = float(input("Enter your weight(kg): "))
unit = input("Is your weight Kilogram or Pounds(K/L): ")
if unit == "K":
    ans = weight * 2.205
    unit = "kgs"
    print(f"Your converted weight is {ans}{unit}")
elif unit == "L":
    ans = weight / 2.205
    unit = "Lbs"
    print(f"Your converted weight is {ans}{unit}")
else:
    print(f"{unit} was not valid")
    # Temperature conversion

unit = input("Enter your unit(K/F) to be converted to degree celsius: ")
figure = float(input("Enter the temperature: "))
if unit == "K":
    celsius = figure - 273.15
    print(f"Your converted {figure}{unit} is {round(celsius, 3)}celsius")
elif unit == "F":
    celsius = (figure - 32) * (5 / 9)
    print(f"Your converted {figure}{unit} is {round(celsius, 3)}{unit}") 
else:
    print(f"This {unit} is not a unit")

# X if condition else Y
number = 10
a = 4
b = 5
print("Even" if number % 2 == 0 else "Odd")
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)


# Validate user input
user_name = input("Enter your name: ")
if len(user_name) > 12:
    print("User Name more than 12 characters")
elif not user_name.find(" ") == -1:
    print("User Name should not contain spaces")
elif not user_name.isalpha():
    print("User Name should not contain digits")
else:
    print(f"Hello {user_name}")



# Formatting specifiers {value: flags}
num1 = 234.55344
num2 = 123.456
num3 = 4335.97978

# number
print(f"The value of number 1 is {num1:.2f}") #234.55
# spaces
print(f"The value of number 2 is {num2:10}") #   123.456
# left justify
print(f"The value of number 3 is {num3:<10}") #4335.97978 
# right justify
print(f"The value of number 3 is {num3:>20}") #          4335.97978
# center align
print(f"The value of number 3 is {num3:^20}") #     4335.97978
# positive
print(f"The value of number 1 is {num1:+}") #+234.55
print(f"The value of number 1 is {num1: }") # 234.55
# thousand separator
print(f"The value of number 3 is {num3:,}") #4,335.97978
# combination
print(f"The value of number 1 is {num1:+,.2f}")#+234.55
print(f"The value of number 2 is {num2: ,.2f}") # 123.46
print(f"The value of number 3 is {num3:+,.2f}") #+4,335.98

# while loop
user_number = int(input("Enter a number between 1 and 10: "))
while user_number < 1 or user_number > 10 :
    print(f"{user_number} is not valid")
    user_number = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {user_number}")

# Python compound interest calculator
principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can not be less than zero")
    else:
        break
while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("Rate can not be less than zero")
    else:
        break
while True:
    time = float(input("Enter the Time: "))
    if time < 0:
        print("Time can not be less than zero")
    else:
        break

final_amount = principal * pow(1 + (rate / 100), time)
print(f"Your total amount after {time} year/s is: ${final_amount:.2f}")

# for loops
for counter in reversed(range(1, 11)): # range(1, 11, -1)
    print(counter)
print("HAPPY NEW YEAR!!!")

# To skip over an iteration use Continue
for x in range(1, 10):
    if x == 3 or x == 5:
        continue
    else:
        print(x) 
# To leave or break from the loop use break
for x in range(1, 10):
    if x == 4:
        break
    else:
        print(x)

        
user_time = int(input("Enter the time in seconds: "))
for x in range(user_time, 0, -1):
    hours = x // 3600
    minutes = (x % 3600) // 60
    seconds = (x % 60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!!!")
'''
# Nested Loop
for count in range(3):
    for x in range(1, 10):
        print(x, end=" ")
    print()

