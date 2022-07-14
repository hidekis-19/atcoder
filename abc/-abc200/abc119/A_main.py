s  = input()

A = list(map(int,s.split("/")))

if A[1]<=4 and A[2]<=30:
    print("Heisei")
else:
    print("TBD")
