target=float(input("target:"))
puzzle=float(input("puzzle:"))
talkingDoll=float(input("talkingdoll:"))
teddyBear=float(input("teddybear:"))
pokemonPlushie=float(input("pkemonplushi:"))
bigToyTruck=float(input("bigtoytruck:"))

totalToys= puzzle + talkingDoll + teddyBear + pokemonPlushie + bigToyTruck

pPrice = puzzle *14
tPrice = talkingDoll * 3
tbPrice = teddyBear *20.2
ppPrice = pokemonPlushie *8.2
bttPrice = bigToyTruck *10.65

totalPrice = pPrice + tPrice + tbPrice + ppPrice + bttPrice

if totalToys < 50:
    money = totalPrice * 0.90
else:
    earn =(totalPrice * 0.75)
    money = earn - (earn * 0.1) 

if money >= target:
    x=money - target
    print(f"Yes! {x:.2f} dollars left.")
else:
    x=target - money
    print(f"Not enough money! {x:.2f} dollars needed.")
