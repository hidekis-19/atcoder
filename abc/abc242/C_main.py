n = int(input())

ans =0

a = 21
b = 4

if n ==2:
    print(25)

for i in range(3,n+1):
    a = 3*a%998244353
    b = 2*b%998244353
print(a+b%998244353)