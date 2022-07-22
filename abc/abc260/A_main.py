s = input()


for ss in list(s):
    if s.count(ss) == 1:
        print(ss)
        exit()
print("-1")