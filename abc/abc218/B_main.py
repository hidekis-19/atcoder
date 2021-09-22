import string
P = list(map(int,input().split()))

l = string.ascii_lowercase


ans = ""

for p in P:
    ans = ans + l[p-1]
print(ans)
