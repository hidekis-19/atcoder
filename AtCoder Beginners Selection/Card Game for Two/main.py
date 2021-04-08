N = int(input())
a = list(map(int, input().split())) 

alise = 0
bob = 0

a_sorted = sorted(a,reverse=True)

for i, ai in enumerate(a_sorted):
    x = i+1
    if x%2 == 1:
        alise += ai
    else:
        bob += ai
print(alise -bob)

