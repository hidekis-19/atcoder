n = int(input())
sList = []
pList = []
for i in range(n):
    s,p = map(str,input().split())
    p = int(p)
    sList.append(s)
    pList.append([p,i])

psum = 0

for p,i in pList:
    psum += p

for p,i in pList:
    if 2*p > psum:
        print(sList[i])
        exit()
print("atcoder")
