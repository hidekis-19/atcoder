import bisect
n = int(input())
num_list = []

def primeNumberCreate():
    primeList = [2]  # 2以下の素数リストを作成
    maxNumber = 1000005 # 1000以下の数字をチェック
    for x in range(3, maxNumber):
        for y in primeList:
            if x % y == 0:
                break
        else:
            primeList.append(x)  # 割り切れるものがなければリストに追加
    return primeList

def indentAdjustment(primeNumbers): # インデント調節のため
    n_list = []
    count = 0
    for num in primeNumbers:
        n_list.append(num)
        count += 1
        if count > 9:
            print(' ')
            count = 0
    return n_list

primeNumbers = primeNumberCreate()
n_list = indentAdjustment(primeNumbers)
ans = 0

for i,a in enumerate(n_list):
    if a >=n:
        break
    for j,b in enumerate(num_list):
        if i < j and n <= a*(b**3):
            ans +=1
print(ans)
            
             
    
        
