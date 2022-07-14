a,b,c = map(int,input().split())

l= [a,b,c]

l = sorted(l,reverse=True)
s = int(str(l[0])+ str(l[1]))

print(s+l[2])
