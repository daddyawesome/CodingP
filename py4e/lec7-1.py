fname = input("Enter the filename: ")
try:
    fhand = open(fname)
except:
    print("File Cannot be opened:", fname)
    quit()
    
count = 0

for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
