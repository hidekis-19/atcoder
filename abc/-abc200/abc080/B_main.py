n = list(input())

x = int("".join(n))

y = 0

for nn in n:
    y += int(nn)

if x%y ==0:
    print("Yes")
else:
    print("No")        