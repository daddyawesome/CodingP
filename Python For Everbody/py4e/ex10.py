fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    wrds = line.split()
    if len(wrds) < 1:
        continue    
    if wrds[0] != 'From':
        continue
    
    word = wrds[5]
    hrs = word.split(':')
    
    counts[hrs[0]] = counts.get(hrs[0],0) + 1

print(counts)

x=sorted(counts.items())

for key,val in x:
    print(key,val)

   
