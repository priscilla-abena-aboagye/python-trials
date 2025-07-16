# Simple Message: Assign a message to a variable, and then print that message
message = "Python here I come"
print(message)
message = "I have to finish this python book"
print(message)

# Use a variable to represent a person's name, and print a message to that person.
# Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.
name = "Cilla"
print(f"Hello {name}")
lower_name = name.lower()
upper_name = name.upper()
title_name = name.title()
print(lower_name)
print(upper_name)
print(title_name)

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

# Find a quote from a famous person you admire. Print the quote and the name of its author. 
quote = "It will suck but I will be okay"
print(f"\t Ryan Holiday once said: {quote}")
