#Python Collections/Dta Structures: TUPLES
#Ordered, not changeable, allows duplicates.

tup_fruits = ["apple", "banana", "cherry"]
print(tup_fruits)

"""
#tup reverse
tup_fruits.reverse()
print(tup_fruits)
"""

tup_scores = (90, 92, 85)
print(max(tup_scores))
print(min(tup_scores))
print(sorted(tup_scores)) #default niya is lowest to highest
print(sorted(tup_scores, reverse=True))  #pwede gawing highest to lowest

#ang tuple ay unchangeable but you can work around it. You can update items by converting it to list and concert it back to tuple
li_scores = list(tup_scores)
li_scores.append(100)
print(li_scores)
tup_scores = tuple(li_scores)
print(tup_scores)