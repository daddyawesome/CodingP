'''

In this mission you should check if all elements in the given list are equal.


Input: List.


Output: Bool.

'''


def all_the_same(numbers):
    if len(numbers) == 0:
        return True
    else:
        nTemp = numbers[0]
            
        for n in numbers:
            if nTemp == n:continue
            else:
                return False
        return True

x1 = [1, 1, 1]
x2 = [1, 2, 1]
x3 = ['a', 'a', 'a']
x4 = []
x5 =[1]
        

print(all_the_same(x1))
print(all_the_same(x2))
print(all_the_same(x3))
print(all_the_same(x4))
print(all_the_same(x5))


#Other solution
def all_the_same2(elements):
   return elements == elements[1:] + elements[:1]

print("Second",all_the_same2(x1))
print("Second",all_the_same2(x2))
print("Second",all_the_same2(x3))
print("Second",all_the_same2(x4))
print("Second",all_the_same2(x5))

#third solution
def all_the_same3(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1

print("THIRD",all_the_same3(x1))
print("THIRD",all_the_same3(x2))
print("THIRD",all_the_same3(x3))
print("THIRD",all_the_same3(x4))
print("THIRD",all_the_same3(x5))
