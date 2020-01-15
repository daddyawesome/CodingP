#Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name "na na boo boo". The program should behave normally for all other files which exist and don't exist.
#
fname = input("Enter file name: ")
boo ='na na boo boo'
if fname == boo:
    print(boo.upper(), 'TO YOU - You have been punk\'d!')
    quit()
else:
    try:
        fhand = open(fname)
    except:
        print("File Cannot be opened:", fname)
        quit()
counter = 0
for line in fhand:
    counter = counter + 1
print("There were",counter, "subject lines in", fname)
