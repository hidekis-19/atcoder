S = list(input())

a = -1
b = -1

for i,s in enumerate(S):
    if s == "A" and a == -1:
        a = i
    if a != -1 and s == "Z":
        b = i

print(b-a+1)


