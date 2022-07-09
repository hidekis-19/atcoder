import sys
input = sys.stdin.readline
n=int(input())
if n==1:
  print(1)
  exit()
dic={}
for i in range(n):
  m=int(input())
  for j in range(m):
    p,e=map(int,input().split())
    if p in dic:
      if dic[p][0]<e:
        dic[p]=(e,i,1)
      elif dic[p][0]==e:
        dic[p]=(e,dic[p][1],2)
    else:
      dic[p]=(e,i,1)

s=set()
for i in dic:
  if dic[i][2]>1:
    continue
  s.add(dic[i][1])
print(min(len(s)+1,n))