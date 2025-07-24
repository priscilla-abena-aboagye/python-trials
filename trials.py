'''

def user_name(name):
	print(f"Hello!, {name}. Nice to meet you.")
user_name("Alice")	

def area_of_rectangle(length, width):
	area = length * width
	return area
ans = area_of_rectangle(3, 4)
print(ans)

def check_status(number):
	if number % 2 == 0:
		print(f"{number} is an even number")
	else:
		print(f"{number} is an odd number")
check_status(22)
'''