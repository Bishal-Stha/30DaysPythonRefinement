# Mutability in list.
A = [1,2,3,4,5]
B = A
B.append(10)
# print(A)

X = [1,3,5,7,9]
Y = X[:] # I want to take the values 3,5,7 from X
Y.append(10)
# print(X)
################################
#string handling.
sentence = "An APPLE A dAY KeePs the doctor away."
# print(sentence.)

sent = "  apple "
print(sent.strip())

word = "bishal@2063"
for l in word:
    if l.isalnum():
        print("Yes it is alphanumeric.")
        break
cleanSent = sentence.lower() 
print(cleanSent)
words = cleanSent.split(" ")
print(words)

friendsForever = "anup,manish,pranish,ujwal,dikshant"
friendsList = friendsForever.split(",")
print(friendsList)