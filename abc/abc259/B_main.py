import math
a,b,d = map(int,input().split())

x = math.radians(d)

c = math.cos(x)*a - math.sin(x)*b
d =  math.sin(x)*a + math.cos(x)*b

print(c,d)