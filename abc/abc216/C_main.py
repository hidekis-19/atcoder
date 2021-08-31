n = int(input())

ans = ""
while n >=2:
    if n%2 ==1:
        n -= 1
        ans =  "A" + ans
    else :
        n = n//2
        ans =  "B" + ans
print("A" + ans)