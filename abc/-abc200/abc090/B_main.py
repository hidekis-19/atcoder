a,b = map(int,input().split())

l = list(range(a,b+1))
ans = 0
for ll in l:
    ll = str(ll)
    x = ll[:int(len(ll)//2)]
    y = ll[-int(len(ll)//2):][::-1]
    if x == y:
        ans += 1
print(ans)
    