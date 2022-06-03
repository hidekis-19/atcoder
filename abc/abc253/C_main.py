import heapq

q = int(input())
S = []
S = heapq.heapify(S)
for i in range(q):
    x = list(input())
    if x[0] == '1':
        heapq.heappush(S, x[2])
    elif x[0] == '2':
        S[x[2]] = max(0,S[x[2]]-x[4])
    elif x[0] == '3':
        ma = 
        mi = S.index[]


        
    

