l1 = [1, 2, 3]
l2 = [10, 20, 30]

for i in l1:
    print('Start outer loop')

    for j in l2:
        print('--', i, j)
        if i == 2 and j == 20:
            print('-- BREAK inner loop')
            break
    else:
        print('-- Finish inner loop without BREAK')
        continue

    print('BREAK outer loop')
    break
# Start outer loop
# -- 1 10
# -- 1 20
# -- 1 30
# -- Finish inner loop without BREAK
# Start outer loop
# -- 2 10
# -- 2 20
# -- BREAK inner loop
# BREAK outer loop