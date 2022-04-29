money =int(input("enter money in cents:"))
dollar = int(money/100)
quarter = int((money%100)/25)
dimes = int((money-(dollar*100+quarter*25))/10)
nickels =int((money-(dollar*100+quarter*25+dimes*10))/5)
pennies =int(money-(dollar*100+quarter*25+dimes*10+nickels*5))
moneys = money /100

print(f"{moneys:} consists of:")
print("Dollars:" , dollar)
print("Quarters:", quarter)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)