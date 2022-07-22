n = int(input())

s = n//3600
n = n%3600
t = n//60
n = n%60

print(str(s).zfill(2)+":"+str(t).zfill(2)+":"+str(n).zfill(2))

