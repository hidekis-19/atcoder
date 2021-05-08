N = input()

if int(N) <=100:
    print(1)

elif N[-2:] == '00':
    print(int(N[:-2]))
else :
    print(int(N[:-2]) +1)

