"""
a={"Name":"Sundhar"}
print(type(a))
"""


a={"Name":"Sundhar",
   "Age":20,
   "Location":"Pannimadai"}

#Modify
a["Age"]=21

#New Key and Values
a["Color"]="Black"

#Update
a.update({"Age":20})

#Delete
a.pop("Color")
print(a)

#Fully Delete
"""
del a
print(a)
"""

   
