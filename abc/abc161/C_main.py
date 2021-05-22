n,k = map(int,input().split())

if n < abs(n-k):
    print(n)
else:
    x = n%k
    print(min(abs(x-k),x))