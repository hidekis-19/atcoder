n = list(input())

s = 0
t = ""
for nn in n:
    s += int(nn)
    t = t + nn

if int(t)%s==0:
    print("Yes")
else:
    print("No")