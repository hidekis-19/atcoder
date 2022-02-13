n = int(input())
st_list = []

for i in range(n):
    inp = list(map(str,input().split()))
    st_list.append(inp)


for st in st_list:
    if st_list.count(st) >=2 :
        print('Yes')
        exit()
print('No')