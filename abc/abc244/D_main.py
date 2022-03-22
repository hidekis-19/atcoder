s = list(map(str, input().split())) 
t = list(map(str, input().split())) 

cnt = 0

for i in range(3):
    if s[i] == t[i]:
        cnt += 1
if cnt == 3:
    print("Yes")
elif cnt ==1:
    print("No")
elif cnt ==0:
    print("Yes")