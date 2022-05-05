num = int(input("Enter a number: "))

checker = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set checker to True
            checker = True
            # break out of loop
            break

# check if flag is True
if checker:
    print("Not Prime")
else:
    print("Prime")