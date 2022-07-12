n = int(input())
t,a = map(int,input().split())
H = list(map(int,input().split()))


ans = 0
high = 999999999999


for i,h in enumerate(H):
    tem = t - h*0.006
    if high > abs(a-tem):
        ans = i+1
        high = abs(a-tem)
print(ans)



