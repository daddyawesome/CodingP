#Write a program to read through a file and print the contents of the file (line by line) all in upper case
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File Cannot be opened:", fname)
    quit()
    
for line in fhand:
    #remove the white after each line
    line = line.rstrip()
    print(line.upper())
