k,x = map(int,input().split())


a = x -k+1
b = x +k-1

c = list(range(a,b+1))
print(" ".join(map(str,c)))
