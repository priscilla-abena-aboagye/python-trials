import math_function
addition = math_function.add(2, 3)
substraction = math_function.substract(5, 2)
mul = math_function.multiply(3, 4)
div = math_function.divide(9, 3)

print(addition)
print(substraction)
print(mul)
print(div)

x = "global  x"
def trials():
    y = "local y"
    print(y)

trials()
print(x)

x = "Global X"
def test():
    x = "Local X"
    print(x)
test()
print(x)

X = "Global X"
def testing():
    global X
    X = "Local X"
    print(X)
testing()
print(X)