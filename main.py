# Improving python skills using Bro Code

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

'''

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




