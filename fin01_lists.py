#Python Collections/Dta Structures: LIST
#Ordered, changeable, allows duplicates.


#indexed     0        1      2     3
#negative indexing -4 -3    -2   -1
li_bsis_names = ["Mathhew", "Ron", "RJ", "JR"] #separator ng list is comma only

#accesing list items
#print(names[-3]) #accepted yung negative number pero hindi siya nagsisisimula sa zero

#accessing list items with range step
#pagi-specify ng range is called slicing
print(li_bsis_names[0:1]) #variable[start:end]
print(li_bsis_names[0:4])
print(li_bsis_names[0:4:2])

#negative indexing with negative step(slicing)
print(li_bsis_names[-1:-4:-2]) #variable[start:end:steps

#negative indexing
print(li_bsis_names[-1:-4:2]) #hindi pwede yung step na 2 since pakanan na siya which is dapat pakaliwa dahil -1 to -4 siya

#changing list item value
li_bsis_names[1]= "Elaine"
print(li_bsis_names[1])
print(li_bsis_names)

#adding item to a list using .append() method
li_bsis_names.append("Nathaniel")
print(li_bsis_names)

#adding item to a list using .insert() method
li_bsis_names.insert(1, "Nathaniel")

#combining list using .extend() method with more than 2 list using + operator
li_act_names = ["Rajj", "Jane", "Prince"]
li_bsis_names.extend(li_act_names)
print(li_bsis_names)

"""
#combining list using .extend() method with more than 2 list using + operator without declaring variable
li_act_names = ["Rajj", "Jane", "Prince"]
li_bssw_names = ["Jael", "Kayla", "Jester", "Yuan"]
li_bab_names = ["K", "Micah", "Jonah"]
li_bsis_names.extend(li_bssw_names + li_act_names + li_bab_names)
print(li_bsis_names)
print(li_bsis_names)
print(li_bsis_names)
"""

"""
#combining list using .extend() method with more than 2 list using + operator without declaring variable
li_act_names = ["Rajj", "Jane", "Prince"]
li_bssw_names = ["Jael", "Kayla", "Jester", "Yuan"]
li_bab_names = ["K", "Micah", "Jonah"]
li_bsis_names.extend(li_bssw_names + li_act_names + li_bab_names)
print(li_bsis_names)
print(li_bsis_names)
print(li_bsis_names)
"""

#combining list using .extend() method with more than 2 list using + operator without declaring variable
li_act_names = ["Rajj", "Jane", "Prince"]
li_bssw_names = ["Jael", "Kayla", "Jester", "Yuan"]
li_bab_names = ["K", "Micah", "Jonah"]
li_bsis_names.extend(li_bssw_names + li_act_names + li_bab_names)
print(li_bsis_names)
print(li_bsis_names)
print(li_bsis_names)


#combining list using .extend() method with more than 2 list using + operator and explicitly declaring variable
li_act_names = ["Rajj", "Jane", "Prince"]
li_bssw_names = ["Jael", "Kayla", "Jester", "Yuan"]
li_bab_names = ["K", "Micah", "Jonah"]
li_names = li_bsis_names + li_act_names + li_bab_names
print(li_names)

#removing item from a list using remove method
li_names.remove("Jane")
print(li_names)

#removing item from a list using del keyword
del li_names[10]
print(li_names)