def func(*args):
    print(args)
#################
def func2(**kwargs):
    print(kwargs)
#####################
func(10,20,30)
func2(a=10, b=20, c=30)
#####################
def addNumbers(*number:int): # so see here, now i don't have to worry about how many values to recieve from user. i can accept any number of arguments from user.
    return sum(number)

result = addNumbers(1,2,3,4,5,6,7,8,9)
print("Sum: ",result)
##########################

def userInfo(**data):
    # print("\n")
    # print(type(data))
    # print(len(data))
    # print(data)
    return data

info = userInfo(name="bishal",age=19, rollno=8, phoneNum="9876543210")

for k,v in info.items():
    print(f"{k}: {v}")
####################################
#Understand Closure
# A closure is a function that remembers variables from its creation scope, even after that scope is gone. 
###################################
# In Python, Scope has following precedence.
"""
LEGB:
Local > Enclosing > Global > Built-in
"""
x = 17
def func2(y):
    z = x+y
    return z

print(func(3))

PI = 3.1415
print(PI)
PI += 4
print(PI)

from typing import Final
E: Final = 2.71
# E+= 10 Now, this works. but it requires to import a module. that's ok.

