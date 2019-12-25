import re
def find_message(text: str) -> str:
    list1 = re.findall(r'[A-Z]',text)
    msg = ""
    for n in list1:
        msg = msg + n
    return msg

if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

   #other solution
def find_message2(text: str) -> str:
    """Find a secret message"""
    return ''.join(filter(str.isupper, text))
