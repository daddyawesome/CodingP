class Robot:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
        
    def introduce_self(self):
        print("My name is "+ self.name)
        print("My color is "+ self.color)
        print("My weight is %i \n"%self.weight)
        
r1 =Robot("Tom","Red",30)
r2=Robot("Jerry","Blue",40)

r1.introduce_self()
r2.introduce_self()

class Person:
    def __init__(self, n, p , i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "Aggressive", False)
p2 = Person("Becky", "Talkative", True)

#p1 own r2
p1.robot_own = r2
p2.robot_own = r1
