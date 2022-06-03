import collections
n = int(input())
s_list = []

for i in range(n):
    s_list.append(input())
    
c = collections.Counter(s_list)
print(c.most_common()[0][0])