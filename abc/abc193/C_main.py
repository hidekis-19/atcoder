n = int(input())
n_s = int(n**0.5)
s = set()

for a in range(2,n_s+1):
    x = a*a
    while x<=n:
        s.add(x)
        x*=a
print(n-len(s))



