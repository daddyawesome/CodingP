#Write a Python script to:
#
#    Display all the prime numbers between 1 to 250.
#    Store the results in a results.txt file.

def is_prime(n):
    """check if prime"""
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

x = range(2, 251)
with open("results.txt", "w") as external_file:

    for n in x:
        if is_prime(n):
            print(n)
            print(n, file=external_file)

external_file.close()