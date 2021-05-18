a,b,c,k= map(int, input().split())

ans = 0

if k<=a:
    ans = k
elif k<= a+b:
    ans = a
else:
    ans = a + -1*(k-b-a)
print(ans)