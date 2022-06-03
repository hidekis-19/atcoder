h,w = map(int,input().split())
s_list = []
maru = []
ma = 'o'

for i in range(h):
    s_list.append(list(input()))

for i in range(h):
    if s_list[i].count(ma)==1:
        maru.append([i,s_list[i].index(ma)])
    elif s_list[i].count(ma)==2:
        maru = [i for i, x in enumerate(s_list[i]) if x == ma]
        print(maru[1]-maru[0])
        exit()

print(abs(maru[0][0]-maru[1][0])+abs(maru[0][1]-maru[1][1]))



