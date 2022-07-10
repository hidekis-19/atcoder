n,x = map(int,input().split())
A = list(map(int,input().split()))

true_list = [False]*(n+1)

true_list[x] = True

while True:
    x = A[x-1]
    if  true_list[x]:
        break
    true_list[x] = True

print(true_list.count(True))    


