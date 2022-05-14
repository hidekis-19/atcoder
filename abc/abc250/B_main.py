n,a,b = map(int,input().split())


ans_list = []

sirokuro1= 0
sirokuro2= 0


for i in range(n):
    x = ""
    sirokuro2 = sirokuro1
    for j in range(n):        
        if sirokuro2 ==0:
            x = x + "."*b
            sirokuro2 =1
        else:
            x = x + "#"*b
            sirokuro2=0
    for k in range(a):
        ans_list.append(x)
    if sirokuro1 ==0:
        sirokuro1=1
    else:
        sirokuro1=0

for ans in ans_list:
    print(ans)