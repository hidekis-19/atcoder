n = input()
len_n = len(str(n))
ans =0
nine = "9"

for i in range(len_n-1):
    ans += int(nine) * (int(nine)+1)//2
    nine = nine + "0"
    
s =int(n) - 10**(len_n-1) +1
ans += s * (s+1)//2
print(ans%998244353)