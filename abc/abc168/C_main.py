import math

a,b,h,m= map(int, input().split())

shita1 = 30*h + 0.5*m
shita2 = 6*m

shita = abs(shita1 -shita2)

x = (a**2 + b**2 -2*a*b*math.cos(math.radians(shita)))**0.5

print(x)