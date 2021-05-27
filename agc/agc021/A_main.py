N = input()

if len(N)>=2:
    x = list(N)[1:]
    y = ['9']*(len(N)-1)
    if x ==y:
        pass
    elif N[0] =='1':
        N = '9'*(len(N)-1)
    else:
        N = str(int(N[0])-1) + '9'*(len(N)-1)

N = [int(n) for n in list(N)]
print(sum(N))
