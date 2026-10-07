# Worksheet 1.2: Task 1 Solution
import sys
grade = int(input("Enter your Grades: "))
if grade <= 100 and grade >= 0:
    if grade <= 100 and grade >= 70:
        print(f"{grade} is a Distinction")
    elif grade < 70 and grade > 40:
        print(f"{grade} is a Pass")
    elif grade < 40 and grade > 0:
        print(f"{grade} is a Fail")
else:
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit("Error!")