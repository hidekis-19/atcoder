import itertools
def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

N = input()
N_list = list(N)
ans = 9999

if digitSum(N)%3==0:
    ans = 0
else:
    for k in range(1,len(N)):
        x = 99999
        for v in itertools.combinations(N_list, k):
            v = [int(s) for s in list(v)]
            if sum(v)%3==0:
                x = len(N) - len(v)
                break
        if x < ans:
            ans = x

if ans==9999:
    ans = -1


print(ans)

