s = input()
t = input()

x,y = 0,0
for i in range(len(s)):
    if s[i] != t[i] :
        if x ==0:
            y = i
        x += 1

if x==0  :
    print("Yes")
elif x==2 and s[y] == t[y+1] and s[y+1] == t[y] :
    print("Yes")
else:
    print("No")
