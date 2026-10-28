#Python Data Structures/Collections: Dictionaries

#Keys - Provinces
#Values - Capital Cities
dict_capital = {
    "Pampanga" : "San Fernando",
    "Cavite" : "Trece Martires",
    "Bulacan" : "Malolos",
    "Bataan" : "Balanga"
}

print(dict_capital)
print(dict_capital["Pampanga"])
print(dict_capital["Bataan"])

'''
dict_bsis_names = {
    0 : "Matthew",
    1 : "Ronn",
    2 : "RJ",
    3 : "JR"
}

print(dict_bsis_names)
print(dict_bsis_names[0])
dict_bsis_names[1] = "Irrad"
print(dict_bsis_names[1])

'''

#Updating value
dict_capital["Pampanga"] = "Angeles"
print(dict_capital["Pampanga"])

del dict_capital["Bulacan"]
print(dict_capital)

dict_car = {
    "brand" : "Ford",
    "model" : "Territory",
    "year" : 2020
}

print(dict_car.get("model"))

dict_cat = {
    "breed" : "Siamese",
    "name" : "Kitty",
    "age" : 3
}

print(dict_cat.get("name"))