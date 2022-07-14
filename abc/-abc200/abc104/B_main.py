s = input()

if s[0] != "A":
    print("WA")
    exit()

if "C" not  in s[2:-1]:
    print("WA")
    exit()
fir =0
for i,ss in enumerate(s):
    if i ==0:
        continue
    elif 2<= i <= len(s)-2:        
        if fir==0 and ss == "C":
            fir +=1
            continue
        elif fir==1 and ss == "C":
            print("WA")
            exit()
    else:
        if not ss.islower():
            print("WA")
            exit()
        
print("AC")
            
    

