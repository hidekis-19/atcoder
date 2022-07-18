a,b,c = map(int,input().split())


s = [a,b,c]

if s.count(7) == 1 and s.count(5) ==2:
    print("YES")
else:
    print("NO")