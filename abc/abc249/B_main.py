S = input()

S_len = len(S)

x = len(set(list(S)))
y = list(S)

if S_len != x :
    print("No")
    exit()

a = 0
b = 0

for s in y:
    if s.islower():
        a = 1


for s in y:
    if s.isupper():
        b = 1

if a ==0 or b==0:
    print("No")
    exit()

print("Yes")