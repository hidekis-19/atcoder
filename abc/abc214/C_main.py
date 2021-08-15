import heapq
n = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

H =[]
ans = [999999999999]*n

for i in range(n):
    H.append([T[i],i])

heapq.heapify(H) 
while H :
    x,y = heapq.heappop(H)
    if x >= ans[y] :
        continue
    ans[y] = x
    heapq.heappush(H, [S[y] + x,(y +1)%n])

for a in ans:
    print(a)




    
