v,a,b,c= map(int, input().split())


while True:
    v = v - a
    if v <0:
        print("F")
        exit()
    v = v - b 
    if v <0:
        print("M")
        exit()
    v = v - c 
    if v <0:
        print("T")
        exit()

