FULLMARKS = 100
PASSMARKS = 40

student = {
    "stdName": str,
    "english": float,
    "nepali": float,
    "math": float,
    "science": float,
    "computer": float
}

totalMarks = 0.0
percentage = 0.0
topper = ""

# percentage = round((totalMarks*100)/(5*FULLMARKS),3) # (total/5*fullmarks)*100

# print(f"{student['stdName']} got {totalMarks} marks and got {round(percentage,2)}%")

n = int(input("Enter how many students: "))
percentages = []
studentNames = []
for k in range(n):
    for i in student:
        if i == "stdName":
            student[i] = input("Enter name: ")
            studentNames.append(student[i])

        else:
            student[i] = float(input(f"Enter {i} marks: "))
            totalMarks = totalMarks + student[i] #
    print("\n")
    percentage = round(((totalMarks*100)/(5*FULLMARKS)),3) # (total/5*fullmarks)*100 (a/b) *c = c* (a/b) = ac/b => totalMarks/5FullMarks * 100 => 100*totalMarks/5*fullMarks
    percentages.append(percentage)
    totalMarks = 0.0

for i,percentage in enumerate(percentages):  
    if percentage <= 100.0:
        if percentage >= 90:
            print(f"{studentNames[i]} scored GPA: A+")
        elif percentage >= 80:
            print(f"{studentNames[i]} scored GPA: A")
        elif percentage >= 70:
            print(f"{studentNames[i]} scored GPA: B+")
        elif percentage >= 60:
            print(f"{studentNames[i]} scored GPA: B")
        elif percentage >= 50:
            print(f"{studentNames[i]} scored GPA: C+")
        elif percentage >= PASSMARKS:
            print(f"{studentNames[i]} scored GPA: C")
        else:
            print(f"{studentNames[i]} got fail.")
        
    else:
        print(f"{studentNames[i]}, Do it seriously. percentage can not exceed 100.")

HSI = percentages.index(max(percentages)) # gives me the index of the max scorer from percentage. (HSI): HigestScorerIndex
print("\n")
print(f"{studentNames[HSI]} became the higest scorer by scoring {percentages[HSI]}%")