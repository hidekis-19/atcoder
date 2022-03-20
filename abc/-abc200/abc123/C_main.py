import math
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = min(a,b,c,d,e)

ans = math.ceil(n/m+4)
print(ans)