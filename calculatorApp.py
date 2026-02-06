def add(x: float, y: float):
    return x + y

def sub(x: float, y: float):
    return x - y

def mul(x: float, y: float):
    return x * y

def div(x: float, y: float):
    if y == 0:
        print("Cannot divide by 0.")
        return None
    return x / y

def power(x: float, y: float):
    return x ** y

def Calculator(x: float, y: float, operation: str):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return sub(x, y)
    elif operation == '*':
        return mul(x, y)
    elif operation == '/':
        return div(x, y)
    elif operation == '^':
        return power(x, y)
    else:
        print("Invalid operation.")
        return None


firstNum = float(input("Enter first number: "))
secondNum = float(input("Enter second number: "))
op = input("Enter operation sign: ")

result = Calculator(firstNum, secondNum, op)

if result is not None:
    print(f"{firstNum} {op} {secondNum} = {result}")
