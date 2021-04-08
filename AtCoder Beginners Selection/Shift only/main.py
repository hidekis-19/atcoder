N = int(input())
A = list(map(int, input().split())) 

ans = 0

#すべて偶数である限り続ける
while True:
    a_cnt = 0
    A_tmp = []
    for i in A:
        if i%2 == 0:
            a_cnt += 1
        A_tmp.append(i/2)
    #すべて偶数かどうかを判定する
    if a_cnt == N:
        ans += 1
    else :
        break
    A = A_tmp

print(ans)






    

        


