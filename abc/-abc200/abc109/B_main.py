n= int(input())
W = []

for i in range(n):
    W.append(input())

s = set()

s.add(W[0])
wend = W[0][-1]


for i,w in enumerate(W):
    if i ==0:
        continue
    if w in s or wend != w[0]:
        print("No")
        exit()
    wend = w[-1]
    s.add(w)
print("Yes")
        