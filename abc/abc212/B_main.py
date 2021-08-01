X = input()

X = list(X)
x1= int(X[0])
x2= int(X[1])
x3= int(X[2])
x4= int(X[3])

if x1 == x2 and x2 == x3 and x3 == x4:
    print('Weak')
elif ((x1 !=9 and x2 == x1+1) or (x1 ==9 and x2 ==0)) and ((x2 !=9 and x3 == x2+1) or (x2 ==9 and x3 ==0)) and ((x3 !=9 and x4 == x3+1) or (x3 ==9 and x4 ==0)):
    print('Weak')
else:
    print('Strong')