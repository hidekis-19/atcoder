n = int(input())
ans = ''
while n:
    if n==0:
        break
    n -= 1
    ans =  chr(ord("a")+n%26) + ans
    n =n//26
print(ans)


