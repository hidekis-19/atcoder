
n = int(input())
L = list(map(int, input().split())) 
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                l = [L[i],L[j],L[k]]
                l = sorted(l)
                if l[2] < l[1]+l[0]:
                    ans +=1

print(ans)