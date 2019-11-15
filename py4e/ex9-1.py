#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the #second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of #times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

han = open("mbox-short.txt")

emails =dict()
for line in han:
    line = line.rstrip()
    wds = line.split()
    
    #Guardian Pattern
    if len(wds) < 1:
        continue
    if wds[0] != 'From':
        continue
    emails[wds[1]] = emails.get(wds[1], 0) +1

maxword = None
maxnum = None

for k,v in emails.items():
    if maxnum is None or v > maxnum:
        maxword = k
        maxnum = v
        
print(maxword,maxnum)
