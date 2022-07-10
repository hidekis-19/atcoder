from collections import deque
from itertools import groupby
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

d = deque()
n = int(input())

for i in range(n):
    x = list(map(int,input().split()))
    x = runLengthEncode(x)
    d.append(x)
ans =0
while d:
    s = d.popleft()
    if d.count(s)!=0:
        d.remove(s)
    ans +=1
print(ans)
    