w = list(input())

for ww in w:
    if w.count(ww) %2 != 0:
        print("No")
        exit()
print("Yes")
        
        