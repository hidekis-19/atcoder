n,l = map(int,input().split())

ringo = []
ins = 9999999999999999999999

for i in range(n):
    ringo.append(l+i)

for rin in ringo:
    if abs(ins)> abs(rin):
        ins = rin
        
print(sum(ringo)-ins)
