n = list(input())

s = ""

for nn in n:
    if nn == "1":
        s = s+ "9"
    elif nn == "9":
        s = s+"1"

print(s)