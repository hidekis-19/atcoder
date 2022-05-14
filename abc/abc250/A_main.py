h,w = map(int,input().split())
r,c = map(int,input().split())

a1 = r-1
a2 = c

b1= r
b2 = c+1

c1 = r+1
c2 = c

d1 = r
d2 = c-1

ans = 0

if 1<= a1 <=h and 1<= a2 <=w:
    ans +=1 
if 1<= b1 <=h and 1<= b2 <=w:
    ans +=1 
if 1<= c1 <=h and 1<= c2 <=w:
    ans +=1 
if 1<= d1 <=h and 1<= d2 <=w:
    ans +=1 
print(ans)
