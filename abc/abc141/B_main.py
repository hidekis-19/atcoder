s = input()


for i,e in enumerate(s):
    if i%2 != 0:
        if e not in ('L','U','D'):
            print('No')
            exit()
    else:
        if e not in ('R','U','D'):
            print('No')
            exit()

print('Yes')
