#add the numbers that are multiples of 3 and 5 
#that is less than 100

total = 0
for i in range(1,100):
    if (i % 3) == 0:
        total +=i
        
    elif (i % 5) == 0:
        total +=i
       
print(total)
