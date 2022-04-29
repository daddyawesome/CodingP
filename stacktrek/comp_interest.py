p =float(input("What is the Principal amount:"))
r =float(input("What is the interest rate:"))
n =float(input("What is the number of years:"))

compound_interest = p *( (1 + (r / 100))**n)

print(f"{compound_interest:.2f}")