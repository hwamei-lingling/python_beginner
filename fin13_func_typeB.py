#Python Function: Type A(no parameters, with return value)

#Function Definition

def random_fruits():
    import random
    i = 0
    list_fruits = ['apple', 'banana', 'mango', 'blueberry']
    while i < 3:
        return random.choice(list_fruits)
    
#Function Invocation
print("Random Fruit:", random_fruits())

