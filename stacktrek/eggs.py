eggs = int(input("the number of eggs:"))
dozenEggs = int(eggs / 12)
remainingEgss = eggs % 12

total_pay = dozenEggs * 70 + remainingEgss * 7

print(total_pay,dozenEggs,remainingEgss)