#Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user.

while True:
    try:
        num =int(input("Please input an integer:"))
    except ValueError:
        print("Sorry, I didn't understand that. Kindly Please enter an integer.")
        continue

    if num < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        break


if num % 2 == 0:
    print("You give an even number.")
else:
    print("You give an odd number")
