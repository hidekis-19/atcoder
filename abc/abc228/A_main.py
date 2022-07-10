s,t,x = map(int,input().split())

if s<t:
    if s<=x and x<=t:
        print("Yes")
    else:
        print("No")
elif s>t:
    if x>=s :
        print("Yes")
    elif x<= t-1:
        print("Yes")        
    else:
        print("No")
