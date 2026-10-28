#Iteration Structure: "for" using collections

#for letter in "La Verdad":
#    print(letter)

fruits = {"Mango", "Banana", "Apple"}
for fruit in fruits:
    print(fruit)


student = {
    "name" : "John",
    "program" : "BSIS",
    "year" : 3,
    "age" : 21
}
'''
for key in student:
    print(student[key])

#or

for key, value in student.items():
    print(key, ":", value)
'''


for key, value in student.items():
    print(key, ":", value)