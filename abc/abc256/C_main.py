h1,h2,h3,w1,w2,w3 = map(int,input().split())

p = 0

for s in range(1,29):
    for t in range(1,29):
        for u in range(1,29):
            for v in range(1,29):
                a1 = s
                a2 = v
                a3 = h1 - s - v
                a4 = w1 - s - h3 + u + w2 - v- t
                a5 = t
                a6 = h2 - w1 + s + h3 - u - w2 + v 
                a7 = h3 - u - w2 + v + t
                a8 = w2 - v - t
                a9 = u
                if 1 <= a3 <=28 and 1 <= a4 <=28 and 1 <= a6 <=28 and 1 <= a7 <=28 and 1 <= a8 <=28 and (a3+a6+u==w3):
                    p += 1

print(p)
    