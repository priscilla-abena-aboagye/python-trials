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