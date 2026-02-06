def factorial(num: int):
    if num <0:
        print(f"{num} is a negative number, enter positive number: ")
        num = int(input())
    fact = 1
    if num == 0:
        return 1
    else:
        for i in range(1,num+1):
            fact *= i
    return fact

n = int(input("Enter number: "))
print(factorial(n))
    