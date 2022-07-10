a,b = map(str,input().split())


aa = list(reversed(list(a)))
bb = list(reversed(list(b)))

if len(aa) >=len(bb):
    for i,bbb in enumerate(bb):
        if int(bbb) + int(aa[i]) >= 10:
            print("Hard")
            exit()   
    print("Easy")
elif len(aa) < len(bb):
    for i,aaa in enumerate(aa):
        if int(aaa) + int(bb[i]) >= 10:
            print("Hard")
            exit()
    print("Easy")
