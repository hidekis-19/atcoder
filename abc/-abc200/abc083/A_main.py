a,b,c,d = map(int,input().split())
 
s = a+ b
t = c+ d

if s == t:
    print("Balanced")
elif s>t:
    print("Left")
elif t>s:
    print("Right")