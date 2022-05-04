import math

num_grade = float(input("Enter grade : "))
if num_grade < 0:
    print("Grade cannot be lesser than zero")
    exit()
elif num_grade > 10:
    print("Grade cannot be greater than ten")
    exit()

a = num_grade % 0.5
if a == 0:
    if num_grade >= 8.5:
        grade = "A"
    elif num_grade >= 7.5:
        grade = "B"
    elif num_grade >= 6.5:
        grade = "C"
    elif num_grade >= 5.5:
        grade = "D"
    else:
        grade = "F"

    print("Grade", grade)
    
else:
    print("Grades should be rounded to the nearest half point.")



