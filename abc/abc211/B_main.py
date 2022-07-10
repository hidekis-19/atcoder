s1 = input()
s2 = input()
s3  = input()
s4  = input()

S = [s1,s2,s3,s4]
if set(["H","2B","3B","HR"]) == set(S):
    print("Yes")
else:
    print("No")