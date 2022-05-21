n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

x_list = []
s = 0

for i,a in enumerate(A):
    if a > s:
        x_list= []
        x_list.append(i+1)
        s = a
    elif a ==s:
        x_list.append(i+1)
        
for x in x_list:
    if x in B:
        print("Yes")
        exit()
print("No")
