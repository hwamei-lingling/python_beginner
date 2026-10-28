#Python Collections/Dta Structures: SETS
#Unordered, changeable, no duplicates (only one "red").
"""
set_ph_pres = {"Emilio Aguinaldo", "Rodrigo Duterte", "Gloria Arroyo", "Bongbong Marcos"}
print(set_ph_pres)

#adding item/s to a set
set_ph_pres.add("Benigno Aquino III")
print(set_ph_pres)

#removing item/s to a set
set_ph_pres.discard("Bongbong Marcos")
print(set_ph_pres)
"""

set_grades_viloria = {"1", "1.25", "1.25", "1.50"}
set_grades_asmollo = {"2", "2.25"}
set_grades_asmollo.add("2.50")
print("Viloria: ", set_grades_viloria)
print("Asmollo: ", set_grades_asmollo)

#using update method in as set
set_grades_asmollo.update(set_grades_viloria)
print("Asmollo (Updated): ", set_grades_asmollo)

#using union method
print(set_grades_asmollo.union(set_grades_viloria))
print(set_grades_asmollo | set_grades_viloria)
print(set_grades_asmollo & set_grades_viloria)