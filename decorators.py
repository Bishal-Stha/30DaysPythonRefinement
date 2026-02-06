# A closure is a function that remembers variables from its enclosing scope, even after that scope has finished execution.

# A decorator is a function that takes another function and returns a new function that extends or modifies its behavior, usually implemented using closures.
##############################################
from closures import func


def my_function():
    print("Doing work")

def wrapper(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner

my_function = wrapper(my_function)
my_function() 
###############################################
def calculator(a: float, b: float, sign: str):
    ops = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
        '%': a % b,
        '//': a // b
    }
    return ops[sign]

print (calculator(10.7,4.3,'+'))
######################################################
def func1():
    print("Apple")

def func2(func):
    def func3():
        print("Ball")
        func()
        print("Cat")
    return func3

func1 = func2(func1)
func1()
#############################################################
