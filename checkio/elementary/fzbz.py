
print("".join(["Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,15)]))
def checkio(number: int) -> str:
    i = number
    x = "".join(["Fizz "*(i%3==0)+"Buzz"*(i%5==0) or str(i)])
    return x 

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
