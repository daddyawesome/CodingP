a = int(input())
b = int(input())
c = int(input())

x = a + b + c

min = int(x/60)
sec = x % 60

if sec < 10:
    print(f"{min}:0{sec}")
else:    
    print(f"{min}:{sec}")
