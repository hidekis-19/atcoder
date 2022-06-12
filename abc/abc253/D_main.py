import math

def lcm(a, b):
    y = a*b / math.gcd(a, b)
    return int(y)

n,a,b= map(int,input().split())

sum_n = n*(n+1)//2
sum_a = (a*(n//a)*((n//a)+1))//2
sum_b = (b*(n//b)*((n//b)+1))//2
sum_ab = ((lcm(a,b))*(n//(lcm(a,b)))*((n//(lcm(a,b)))+1))//2

print(sum_n-sum_a-sum_b+sum_ab)
