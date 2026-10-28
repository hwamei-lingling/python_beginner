#Using collections within a collection

#LISTS AS OUTER STRUCTURE

#List within a list
list_in_a_list = [["A", "a"], ["B", "b"], ["C", "c"]]

print(list_in_a_list[2][1])

#Dictionary witin a list
'''dict_in_a_list = [
    { "brand" : "Toyota", "model" : "Innova", "year" : 2014 },  #0
    { "brand" : "Honda", "model" : "City", "year" : 2019},  #1
    { "brand" : "Suzuki", "model" : "Jimny", "year" : 2016}  #2
]

print(dict_in_a_list[1]["brand"], dict_in_a_list[1]["model"])'''

#DICTIONARY AS OUTER STRUCTURE

#Dictionary witin a list
dict_in_a_dict = {
    "car1" : { "brand" : "Toyota", "model" : "Innova", "year" : 2014 },
    "car2" : { "brand" : "Honda", "model" : "City", "year" : 2019},
    "car3" : { "brand" : "Suzuki", "model" : "Jimny", "year" : 2016}
}

print(dict_in_a_dict["car3"]["brand"], dict_in_a_dict["car3"]["model"])