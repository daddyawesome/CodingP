class Robot:
    def introduce_self(self):
        print("My name is "+ self.name) # This in Java
        
r1 =Robot()
r1.name = "Tom"
r1.color = "Red"
r1.weight = 30

r2=Robot()
r2.name = "Jerry"
r2.color = "Blue"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()
