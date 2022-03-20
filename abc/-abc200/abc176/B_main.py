n = input()
n = list(n)

nine = 0
ans = 'No'
for i in n:
    nine += int(i)

if nine %9==0:
    ans = 'Yes'
print(ans)
