a,b = map(int,input().split())
s = list(input())

t = s.pop(a)

if t != "-" or len(s) != a+b:
    print("No")
    exit()
for ss in s:
    if not str.isnumeric(ss):
        print("No")
        exit()

print("Yes")        
    

