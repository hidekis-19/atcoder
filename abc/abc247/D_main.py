from collections import deque
tsutsu = deque()
n = int(input())
q_list = []

for i in range(n):
    q_list.append(list(map(int,input().split())))

for q in q_list:
    if q[0] == 1:
        tsutsu.append([q[1],q[2]])   
    else:
        if tsutsu == []:
            print()
            continue
        ans = 0
        s = q[1]
        while True:
            x = tsutsu.popleft()
            if s <= x[1]:
                ans += s*x[0]
                tsutsu.appendleft([x[0],x[1]-s])
                break
            else:
                ans += x[0]*x[1]
                s -= x[1]
        print(ans)
           
    
