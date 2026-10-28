#LIST AS OUTER STRUCTURE

print("*** LIST AS OUTER STRUCTURE ***\n")

print("-- List within a List --")
list_in_list = [[1, 2], [3, 4]]
print(list_in_list[0])        # [1, 2]
print(list_in_list[1][0])     # 3

print("-- Tuple within a List --")
tuple_in_list = [(1, 2), (3, 4)]
print(tuple_in_list[0])       # (1, 2)
print(tuple_in_list[1][1])    # 4

print("-- Dictionary within a List --")
dict_in_list = [{"name": "Alice"}, {"name": "Bob"}]
print(dict_in_list[0])        # {'name': 'Alice'}
print(dict_in_list[1]["name"])# Bob

print("-- Set within a List --")
set_in_list = [{"apple", "banana"}, {"cherry"}]
print(set_in_list[0])         # {'apple', 'banana'}
print("banana" in set_in_list[0])  # True


print("\n\n*** TUPLE AS OUTER STRUCTURE ***\n")

print("-- List within a Tuple --")
list_in_tuple = ([1, 2], [3, 4])
print(list_in_tuple[1])       # [3, 4]
print(list_in_tuple[0][1])    # 2

print("-- Tuple within a Tuple --")
tuple_in_tuple = ((1, 2), (3, 4))
print(tuple_in_tuple[1])      # (3, 4)
print(tuple_in_tuple[1][0])   # 3

print("-- Dictionary within a Tuple --")
dict_in_tuple = ({"id": 1}, {"id": 2})
print(dict_in_tuple[0])       # {'id': 1}
print(dict_in_tuple[1]["id"]) # 2

print("-- Set within a Tuple --")
set_in_tuple = ({"a", "b"}, {"c"})
print(set_in_tuple[0])        # {'a', 'b'}
print("a" in set_in_tuple[0]) # True


print("\n\n*** SET AS OUTER STRUCTURE ***\n")

print("-- Tuple within a Set --")
tuple_in_set = {(1, 2), (3, 4)}
for t in tuple_in_set:
    print(t)   # prints each tuple (order not guaranteed)

# Access example:
# You cannot index sets directly since they are unordered.
# But you can loop or convert to a list:
print(list(tuple_in_set)[0][1])  # Access tuple element


#NOT ALLOWED
# set_in_set = {{1, 2}, {3, 4}}   # ❌ Error (set is unhashable)
# list_in_set = {[1, 2], [3, 4]}  # ❌ Error
# dict_in_set = {{'a': 1}}        # ❌ Error



print("\n\n*** DICTIONARY AS OUTER STRUCTURE ***\n")

print("-- List within a Dictionary --")
list_in_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "prices": [10, 20, 30]
}
print(list_in_dict["fruits"])        # ['apple', 'banana', 'cherry']
print(list_in_dict["fruits"][1])     # banana

print("-- Tuple within a Dictionary --")
tuple_in_dict = {
    "pointA": (1, 2),
    "pointB": (3, 4)
}
print(tuple_in_dict["pointA"])       # (1, 2)
print(tuple_in_dict["pointB"][0])    # 3

print("-- Set within a Dictionary --")
set_in_dict = {
    "vowels": {"a", "e", "i", "o", "u"},
    "numbers": {1, 2, 3}
}
print(set_in_dict["vowels"])         # {'a', 'e', 'i', 'o', 'u'}
print("e" in set_in_dict["vowels"])  # True

print("-- Dictionary within a Dictionary --")
dict_in_dict = {
    "student1": {"name": "Ana", "grade": 90},
    "student2": {"name": "Ben", "grade": 85}
}
print(dict_in_dict["student1"])           # {'name': 'Ana', 'grade': 90}
print(dict_in_dict["student2"]["grade"])  # 85



print("\n\n*** COMPLEX/MULTI LEVEL EXAMPLES ***\n")

print("-- Dictionary → List → Dictionary --")
school = {
    "students": [
        {"name": "Alice", "grades": [90, 85, 88]},
        {"name": "Bob", "grades": [75, 80, 82]}
    ]
}
print(school["students"][0]["grades"][2])  # 88

print("-- List → Dictionary → Set --")
example = [
    {"colors": {"red", "green"}},
    {"fruits": {"apple", "banana"}}
]
print("red" in example[0]["colors"])  # True

print("-- Tuple → Dictionary → List --")
nested = (
    {"marks": [95, 90]},
    {"marks": [80, 85]}
)
print(nested[1]["marks"][0])  # 80

print("-- Dictionary with Tuple key → List value --")
data = {
    ("Alice", "Math"): [90, 95],
    ("Bob", "Science"): [85, 88]
}
print(data[("Bob", "Science")][1])  # 88