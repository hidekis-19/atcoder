n,q = map(int,input().split())
A = list(map(int,input().split()))
K = []

for i in range(q):
    K.append(int(input()))
                
            

def binary_search_find_closest(data, target):
    
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    min_diff = float('inf')
    imin = 0
    imax = len(data) - 1
    closest_num = None
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        #　中心の左右の値と目標との差を計算する。
        if imid + 1 < len(data):
            min_diff_right = abs(data[imid+1] - target)
        if imid > 0:
            min_diff_left = abs(data[imid-1] - target)
        # 最初の差と最も最小に近い値を更新する。
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[imid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[imid+1]
        # 2分探索する。
        if data[imid] < target:
            imin = imid + 1
        elif data[imid] > target:
            imax = imid -1
        else:
            return data[imid]
    return closest_num




for k in K:
    x = binary_search_find_closest(A, k)
    print(x)
        


