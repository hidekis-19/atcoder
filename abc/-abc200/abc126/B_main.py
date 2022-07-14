S = list(input())

a = int(S[0] + S[1])
b = int(S[2] + S[3])

if 1<=a<=12 and 1<=b<=12:
    print("AMBIGUOUS")
elif 1<=b<=12  and 0<=a<=99:
    print("YYMM")  
elif 1<=a<=12 and 0<=b<=99:
    print("MMYY")
else:
    print("NA")

