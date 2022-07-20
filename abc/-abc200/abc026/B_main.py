n = int(input())
R = []

for i in range(n):
    R.append(int(input()))
    
R = sorted(R,reverse=True)
ans = 0
for i,r in enumerate(R):
    if i%2 ==0:
        ans += r*r*3.14159265358979323846
    else:
        ans -=  r*r*3.14159265358979323846

print(ans)