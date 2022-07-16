s = list(input())

a = [chr(i) for i in range(97, 97+26)]
for i in a:
    if i not in s:
        print(i)
        exit()
print("None")