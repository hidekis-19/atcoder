import heapq
n,k = map(int,input().split())
P = list(map(int,input().split()))

card = [[] for _ in range(n)]
ans = [-1]*(n+1)
que = []
heapq.heapify(que)


for i,p in enumerate(P):
    if len(que) :
        x = heapq.heappop(que)
        if p> x:        
            heapq.heappush(que,p)
        else:
            card[p].extend(card[x])
            card[x] = []
            if len(card[p]) == k:
                for c in card[p]:
                    ans[c] = i + 1
            else:
                heapq.heappush(que,p)                
                heapq.heappush(que,x)
    else:
        heapq.heappush(que,p)
    print(que,"/",card,"/",ans)


for a in ans[1:]:
    print(a)                
    
    
