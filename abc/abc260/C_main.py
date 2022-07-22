n,x,y =map(int,input().split())

ans = 0
red = [0]*(n+1)        
blue = [0]*(n+1)

red[n] = 1

for i in sorted(list(range(2,n+1)),reverse=True):
    s = red[i]
    red[i-1] += s
    blue[i] += s*x
    red[i] = 0
    t = blue[i]
    red[i-1] += t
    blue[i-1] += t*y
    blue[i] =0

print(blue[1])
    
    
    
        

    
