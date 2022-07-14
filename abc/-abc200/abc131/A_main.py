S = input()

s = S[0]

for i in range(1,len(S)):
    if s == S[i]:
        print("Bad")
        exit()
    else:
        s = S[i]
print("Good")