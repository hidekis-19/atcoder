S = input()
ans = 0

for i in range(10000):
    i = list(str(i).zfill(4))
    t = True
    for j in range(10):
        if (S[j] == 'o' )and (str(j) not in i):
            t = False
        elif (S[j] == 'x' )and (str(j)  in i):
            t = False
    if t :
        ans +=1
print(ans)
