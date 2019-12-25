import re
def checkio(text):

    text = text.lower()
    list1 = re.findall(r'[a-zA-Z]',text)
    set1 = set(list1)
    times = []
    for i in set1:
        times.append(list1.count(i))
    d = dict(zip(set1,times))
    d1 = sorted(d.items(),key = lambda x: (-x[1], x[0])) 
    return d1[0][0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("AAaooo!!!!"))

#count the alphabet, the numbers and the special
string = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

#brilliant solution
import string
def checkio2(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
print(checkio2("AAaooo!!!!"))


#other solution
from string import ascii_lowercase as letters
checkio = lambda text: max(letters, key=text.lower().count)

