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
