from collections import deque
s = deque(list(input()))
t = deque(list(input()))

for i in range(len(s)+1):
    if s ==t:
        print("Yes")
        exit()
    s.rotate()

print("No")
