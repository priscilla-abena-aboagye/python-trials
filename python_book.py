# Simple Message: Assign a message to a variable, and then print that message
message = "Python here I come"
print(message)

# Assign a message to a variable, and print that message.
#  Then change the value of the variable to a new message, and print the new message.
message_2 = "The cat is a motivator"
print(message_2)
message_2 = "I have to finish this python book"
print(message_2)

# Use a variable to represent a person's name, and print a message to that person.
name = "Cilla"
print(f"Hello {name}")

# Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.

name_2 = "Bismark"
lower_name = name_2.lower()
upper_name = name_2.upper()
title_name = name_2.title()
print(lower_name)
print(upper_name)
print(title_name)

# Find a quote from a famous person you admire. Print the quote and the name of its author. 
quote = "It will suck but I will be okay"
print(f"\t Ryan Holiday once said: {quote}")


'''
Use a variable to represent a person's name, and include 
some whitespace characters at the beginning and end of the name. Make sure 
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip()
'''
name_3 = " Abena "
print(f"\t {name_3}")
print(name_3.lstrip())
print(name_3.rstrip())
print(name_3.strip())
