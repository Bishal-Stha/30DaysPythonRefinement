# DataTypes in Python
# Numerical
# Dictionary
# Boolean
# Set
# Sequence type
##################
# Numerical: int, float and complex 
comp = 2+3j
comp2 = 3+4j
print(comp+comp2) # 5+7j

userData = {"name":"bishal", "age": 20}
userAge = userData["age"] # returns 20

print(userAge)

#############################
#let's learn about list in python.
friends = ["Alok","Anish",49,5,True, 3.0]
print(friends)

# const int PI = 3.1415;
from typing import Final
PI:Final = 3.1415 
print(PI)
# PI+= 1

print(PI)
##############################
age = int(input("Enter age: "))
if age >=18:
    print("You can vote")

else:
    print("You're not eligible for voting.")

