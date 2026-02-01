def f(x=[]):
    x.append(1)
    return x

print(f())
print(f([20,30,40])) # this function will fail because it can not handle the function argument. No matter what user inputs, the output is always same and recurring on calling it appends another 1 and one after another.


a = [1, 2, 3]
b = a # b = [1,2,3]
b.append(4) # b = [1,2,3,4]
print(a) # a = [1,2,3,4]

"""
    List a, b ma assign bhayo. then, maile b ma 4 append garda chai a pani badho. but integer haru ma like,
    a = 10
    b = a
    b+=1
    print(a,b) # a = 10, 11 
    yesma chai feri a chai badhdaina.
"""
#################################
a = [1, 2, 3]
b = a[:]
b.append(4) # [1,2,3]
print(a, b) # [1,2,3] [1,2,3,4]
#################################
a = 10
b = a # b = 10
b += 1 # b = 11
print(a, b) # 10 11
#################################
def modify(x):
    x.append(100)

lst = [1, 2, 3]
modify(lst) # lst = [1,2,3,100]
print(lst) # [1,2,3,100]
################################
def removeDuplicates(statement: str):
    unique_words = []
    words = statement.split(sep=" ")
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    st = " ".join(unique_words)
    return st

print(removeDuplicates("My name name is is is Bishal Bishal"))
            

