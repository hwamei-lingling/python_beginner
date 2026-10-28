#Python Function: TYPE C(with parameters and No Return value)

#Function Definition
def add(n1, n2):
    print(n1, "+", n2, "=", n1 + n2)
#main
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
add(num1, num2) #Function Invocation


def square(num):
    print("the square of", num, "is", num**2)

n = int(input("Enter a number: "))
square(n)
