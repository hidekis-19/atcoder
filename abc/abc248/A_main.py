S = input()

l = ["0","1","2","3","4","5","6","7","8","9"]

S = list(S)

for x in l :
    if x not in S:
        print(x)
        exit()
    

