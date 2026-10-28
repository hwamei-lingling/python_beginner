#Python Function: Type D(with parameters and Return value)

def odd_or_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        return "odd"

#main
n = int(input("Enter first number: "))
print(n, "is an", odd_or_even(n), "number")
