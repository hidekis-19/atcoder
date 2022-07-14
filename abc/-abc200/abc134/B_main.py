n,d = map(int,input().split())

x = n//(2*d+1)
y = n%(2*d+1)    

if y !=0:
    print(x+1)
else:
    print(x)