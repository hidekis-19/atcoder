n = int(input())


price = []
for i in range(n):
    price.append(int(input()))

print(sum(price)-max(price)+max(price)//2)
    