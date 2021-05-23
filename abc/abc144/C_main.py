n = int(input())

nn = int(n**0.5) +1
ans = 10000000000000
for i in range(1,nn+1):
    if n%i ==0:
        x = n//i
        ans = min(ans,i+x-2)
print(ans)
