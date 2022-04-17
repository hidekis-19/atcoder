n = int(input())
t = input()

t_l = list(t)
x = 0
y = 0
z = 0
for a in t_l :
    if a == "S":
        if z == 0:
            x += 1
        elif z == 90:
            y -= 1
        elif z == 180:
            x -= 1
        elif z == 270:
            y += 1
    else:
        z += 90
    z = z%360
        
print(x,y)