n = list(input())

for nn in n:
    if n.count(nn) != len(n):
        print("DIFFERENT")
        exit()
print("SAME")