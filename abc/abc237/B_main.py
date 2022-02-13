h,w = map(int, input().split())
A = []
for i in range(h):
    A.append(list(map(int,input().split())))

tr = list(zip(*A))
for t in tr:
    print(' '.join(map(str,t)))
    
    