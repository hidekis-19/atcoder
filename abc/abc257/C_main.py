import bisect
n = int(input())
s = input()
W = list(map(int,input().split()))

ada = []
chi = []

for i,ss in enumerate(list(s)):
    if ss == "0":
        chi.append(W[i])
    elif ss == "1":
        ada.append(W[i])

chi = sorted(chi)
ada = sorted(ada)    


ans1 = 0
chi_cnt = len(chi)

ans2 = 0
ada_cnt = len(ada)

for i,c in enumerate(chi):
    x = bisect.bisect_left(chi,c+1) 
    y = bisect.bisect_left(ada,c+1)
    ans1 = max(ans1,x+ada_cnt-y)

for j,a in enumerate(ada):
    x = bisect.bisect_left(chi,a)
    y = bisect.bisect_left(ada,a)
    ans2 = max(ans2,ada_cnt-y +x)

print(max(ans1,ans2))
    
    

