i = list(map(int, input().split())) 

i = sorted(i,reverse=True)
ans = 'No'
if (i[0]-i[1]) == (i[1]-i[2]):
    ans = 'Yes'

print(ans)