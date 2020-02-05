#This the most important lecture notes
#This will count the most number of words in the file
#
name = input('Enter File:')
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    
    for wds in words:
        counts[wds] = counts.get(wds, 0) +1

maxword = None
maxnum = None

for key,val in counts.items():
    if maxnum is None or val > maxnum:
        maxword = key
        maxnum = val
        
print(maxword,maxnum)
