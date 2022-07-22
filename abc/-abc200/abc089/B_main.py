n = int(input())
S = list(map(str,input().split()))

s = len(set(S))

if s ==3:
    print("Three")
elif s== 4:
    print("Four")


