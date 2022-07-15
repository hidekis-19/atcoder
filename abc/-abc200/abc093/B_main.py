a,b,k = map(int,input().split())

s = []

for i in range(0,k):
    if a <=a+i <= b:    
        s.append(a+i)
    if a<= b-i <= b:
        s.append(b-i)
s = sorted(list(set(s)), reverse= False)

for ss in s:
    print(ss)
