import bisect
L = [0,1,2,3,4,5,6,7]

s = bisect.bisect_left(L,1)
t = bisect.bisect_left(L,4)
u = bisect.bisect_right(L,3)
print(s,t,u)
        