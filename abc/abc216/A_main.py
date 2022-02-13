a = input()

x = a.split('.')[0]
y = int(a.split('.')[1])

if y <=2:
    print(x + '-')
elif y <=6:
    print(x)
else:
    print(x + '+')