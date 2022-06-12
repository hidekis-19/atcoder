s = input()
t = input()

alfa = [chr(ord("a")+i) for i in range(26)]
alfa2 = alfa + alfa

u = ""

x = alfa.index(t[0]) - alfa.index(s[0])

if x <0:
    x += 26        
for i in range(len(s)):
    a = alfa2[x+alfa.index(s[i])]
    u = u+a

if t == u:
    print("Yes")
else:
    print("No")
    