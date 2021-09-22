s1 = input()
s2 = input()
s3 = input()
t = input()

S = [s1,s2,s3]

ans = ""

for i in t:
    ans = ans + S[int(i)-1]
print(ans)
