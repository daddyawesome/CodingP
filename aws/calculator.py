def calculator(a, b, formula):    
    if formula == "+" or formula == "add":
        sum = a + b
        print("Sum:",sum)
    elif formula == "-" or formula == "subtract":
        diff = a - b
        print("Difference:",diff)
    elif formula == "*" or formula == "multiply":
        prod = a * b
        print("Product:",prod)
    elif formula == "/" or formula == "divide":
        quotient = a / b
        print("Quotient:",quotient)
    elif formula == "%" or formula == "remainder":
        prod = a % b
        print("Remainder :",prod)
n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
operation = input("Operation:" )

calculator(n1,n2,operation)
