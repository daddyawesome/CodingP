han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    wds = line.split()
    
    #Guardian in a compound statement
    if len(wds) < 1 or wds[0] != 'From':
        continue
    print(wds[2])
