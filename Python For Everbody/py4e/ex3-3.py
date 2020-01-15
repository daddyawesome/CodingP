#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

score = input("Please enter your score:")
try:
  s = float(score)
except:
  print("Error, please enter numeric input")
  quit()

if s > 1:
    print("I cannot grade your score because it is greater than 1")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0:
    print("I cannot grade your score because it is lesser than 0")
elif s < 0.6:
    print("F")
