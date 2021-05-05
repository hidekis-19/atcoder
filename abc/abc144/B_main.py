N = int(input())
ans = 'No'

for i in range(9):
    x = i+1
    a = N/x
    b = N%x
    if (1<= a ) and (a<=9) and (b==0):
        ans = 'Yes'
print(ans)
