#Iteration Structure: "for" using range() function

num = int(input("Enter a number: "))

for j in range(num):
    for i in range(j):
        print("* ", end="")
    print()