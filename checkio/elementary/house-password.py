import re
def checkio(p: str) -> bool:
    x = True

    if (len(p)<10):
        x=False
    elif not re.search("[a-z]",p):
        x=False
    elif not re.search("[0-9]",p):
        x=False
    elif not re.search("[A-Z]",p):
        x=False
    else:
        print("Valid Password")

    return x    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

 #other solution
def checkio2(data):
    return True if re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$", data) and len(data) >= 10 else False

def checkio3(data):
    # (?=) is positive lookahead. Use this construction to make sure the enclosed pattern exists
    return bool(re.search(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}$', data))
