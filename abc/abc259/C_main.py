from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

S = input()
T = input()

s = runLengthEncode(S)
t = runLengthEncode(T)

for i,tt in enumerate(t):
    if i == len(s):
        print("No")
        exit()        
    if tt == s[i]:
        continue
    elif tt[0] == s[i][0] and s[i][1]>=2 and tt[1]>=s[i][1]:
        continue
    else:
        print("No")
        exit()
print("Yes")
    