n,m,k= map(int, input().split())

def get_integral_value_combination(list, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
    return a(0, [], [], target)

list = []

for i in range(1,n+1):
    list.extend([i]*m)

print(get_integral_value_combination(list, k))