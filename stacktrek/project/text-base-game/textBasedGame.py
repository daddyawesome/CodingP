import time, random

def status(lvl,hp,xp):
    print(f"\n********\nSTATUS\nLevel: {lvl}\nHP: {hp}\nEXP: {xp}\n********\n")

def die(name):
    print("Farewell, " + name + ".")
    quit()

def level(xp):
    if xp < 10:
        lvl = 0
    elif xp <= 20:
        lvl = 1
    elif xp <= 30:
        lvl = 2
    elif xp <= 40:
        lvl = 3
    else:
        lvl = 4
    
    return lvl

def waitForIt():
    print("***")
    print("**")
    print("*")
    time.sleep(1)
    print("Wait for it….\n...\n..\n.")
    time.sleep(2)

def waitForIt2():
    print("Wait for it….")
    print("***")
    print("**")
    print("*")
    time.sleep(1)

def rockwallf():
    print("There is a wall in front of you.\nYou tried to scale the wall.\nYou stamina is not enough to reach the top.\nYour hand slip.\nYou died!!!.\n\n")
    die(name)

def lakef():
    death =random.choice(["You just realized that you don't know how to swim and the lake is very deep, you drowned","The lake is full of aquatic monsters","The lake is just an illusion it was actually a void"])
    print("There is a lake in front of you.\nIt looks enchanting.\nYou feel dirty and you want to swim.\nYou jump towards the lake shouting \"Geronimo!!!\" \n"+death+" \nYou died!!!.\n\n")
    die(name)

def goalf():
    print("Congratulation!!!\nYou have survive the trial phase.\nYou are now an official adventurer.\nIn the land of\n...\n..\n.")
    waitForIt()
    print("The END!!!")
    print("see you next chapter!!!")
    quit()

def slimef(classMW):
    print("You found a slime...")
    if classMW == "warrior":
        print("You are warrior, you try to fight with the slime. \nSlime is immune to physical attack.")
        print("The slime figth back.\nYou died!!!")
        die(name)
    elif classMW == "mage":
        print("You are mage, you throw a fireball to the slime. \nThe slime dies.")
        print("You won the battle. \nyou've gain some experience.")
    
    
def salamanderf(classMW):
    print("You found a salamander...")
    if classMW == "warrior":
        print("You are warrior, you try to fight with the salamander. \nYou slash it with your wooden sword.")
        print("The salamander tried to figth back.\nBut you never stop slashing until it dies..")
        print("You won the battle. \nyou've gain some experience.")
    elif classMW == "mage":
        print("You are mage, you throw a fireball to the salamander. \nThe Salamander is immune to your fireball.")
        print("The salamander figths back.\nYou died!!!")
        die(name)
        
    

def hrabbitf(lvl):
    print("You found a horny rabbit...")
    print("This horny rabbit is extremely aggresive and tried to penetrate you with its horn")
    
    if lvl < 1:
        print("You are not strong enough for the horny rabbit.")
        print("You have been stab again and again. \nYou died!!!")
        die(name)
    else:
        print("You fight back by deflecting its horn with your awesomeness.")
        print("You are stronger than the horny rabbit.")
        print("You won the battle. \nyou've gain some experience.")


def orcf(lvl):
    print("You found a orc...")
    print("The orc found you...")
    waitForIt()
    if lvl < 3:
        print("\nYou died!!!")
        die(name)
    else:
        print("You are stronger than the orc.")
        print("You won the battle. \nyou've gain some experience.")

# Introduction
print("Hello there, HOOMAN. I am your guide to this next life.")
print("What do I mean by next life. This is your life after you earthlife. (^-^)")
name = input("What is do you like to be called as, Hooman?\n>>> ")

#class change
print("Greetings, hooman named " + name + ". Let us start by choosing a class!")
print("To start living in this new world you must have a class.")
classMW = ""
mage_warrior=["warrior", "mage"]

while classMW not in mage_warrior:
    classMW = input("We have two available class for you warrior and mage.\nWhich do you Choose?\n>>> ")
    classMW = classMW.lower()
    if classMW == "warrior":
        print("You have chosen to be a warrior " + name + ".\nTake this wooden sword to begin your warrior journey")
        
    elif classMW == "mage":
        print("You have chosen to be a mage " + name + ".\n take this wooden stick to begin your magical journey")
    
    else:
        print("I didn't understand that.\nPlease die")
        die(name)

waitForIt()

print("You are now in the center of a dark forest.\nYour quest is to find the exit.")
print("Will you accept this quest?\n")
quest1 =input(">>> ")

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
directions = ["left", "right", "forward", "backward"]

#initialize
looper = True
x = 4
y = 4
lvl = 0
hp = 2
xp = 0

slime = ["1,4","3,4","5,4","5,3"]
goal=["1,6","1,7","7,5","7,6"]
lake = ["5,1","6,1","6,2","7,1","7,2","7,3","7,4"]
rockwall = ["1,1","1,2","1,3","2,1"]
salamander = ["4,1","4,3","4,5","3,6"]
hrabbit = ["2,2","2,5","4,7","5,2","6,4","6,7"]
orc = ["1,5","2,6","2,7","6,5","6,6","7,7"]

status(lvl,hp,xp)

if quest1 in yes:
    while looper:
        response = input("What direction do you move?\neast(e)/west(w)/north(n)/south(s)\n>>>")
        if response == "east" or response == "e":
            print("You Choose east and then ...")
            waitForIt2()
            x -=1

        elif response == "west" or response == "w":
            print("You Choose west and then ...")
            waitForIt2()
            x +=1

        elif response == "north" or response == "n":
            print("You Choose north and then ...")
            waitForIt2()
            y -=1

        elif response == "south" or response == "s":
            print("You Choose south and then ...")
            waitForIt2()
            y +=1

        else:
            print("I didn't understand that.\n")
            continue

        if 7< x or x < 1 or 7 < y or y < 1:
            print("You have stepped into the void!")
            die(name)

        xy =f"{x},{y}"
        
        if xy in rockwall:
            rockwallf()
        elif xy in lake:
            lakef()
        elif xy in goal:
            goalf()
        elif xy in slime:
            slimef(classMW)
            xp += 6
        elif xy in salamander:
            salamanderf(classMW)
            xp += 6
        elif xy in hrabbit:
            hrabbitf(lvl)
            xp += 11
        elif xy in orc:
            orcf(lvl)
            xp += 12
        else:
            print("There is nothing here.\nIt is just the forest.")
            

        lvl = level(xp)
        status(lvl,hp,xp)

else:
    print("There is nothing I can do for you. \nYou are hopeless.")
    die(name)