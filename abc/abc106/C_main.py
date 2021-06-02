s = input()
k = int(input())


for i in range(len(s)):
    if k > pow(int(s[i]),500):
        k -= pow(int(s[i]),500)
    else:
        print(s[i])
        exit()
    
    
