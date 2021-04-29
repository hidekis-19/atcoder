import sys
H,W,X,Y= map(int, input().split())

S = []
for i in range(H):
    S.append(list(input()))

ans = 1

x = X-1
y = Y-1


#top 
for i in range(1,X):
    a = x -i
    if S[a][y] == '.':
        ans += 1
    else:
        break

#left
for i in range(1,Y):
    b = y -i
    if S[x][b] == '.':
        ans += 1
    else:
        break

#right
for i in range(1,W-Y+1):
    b = y +i
    if S[x][b] == '.':
        ans += 1
    else:
        break

#bottom
for i in range(1,H-X+1):
    a = x+i
    if S[a][y] == '.':
        ans += 1
    else:
        break


print(ans)
