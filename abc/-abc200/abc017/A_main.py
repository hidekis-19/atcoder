s1,e1 = map(int,input().split())
s2,e2 = map(int,input().split())
s3,e3 = map(int,input().split())

ans = 0

ans += s1*e1*0.1
ans += s2*e2*0.1
ans += s3*e3*0.1
print(int(ans))