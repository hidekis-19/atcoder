s = int(input())

l = [111,222,333,444,555,666,777,888,999]
t = []

for ll in l:
    if ll >= s:
        t.append(ll)

print(min(t))     



    