import itertools
n = input()
n_list = list(n)

ans = 0
for i in range(1,len(n)//2+1):
    s_list = list(itertools.combinations(n,i))
    for s in s_list:
        s = list(s)
        n_list = list(n)
        #最初のものだけ取り除くようにするスマートな方法を考えたい
        for si in s:
            n_list.remove(si)
            
        ss = sorted(s,reverse=True)
        tt = sorted(n_list,reverse=True)
        sss = int("".join(ss))
        ttt = int("".join(tt))
        ans = max(ans,sss*ttt)
print(ans)
        



    





