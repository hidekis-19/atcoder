s = input()

t = [0,0,0,0,0,0]

t[0] = s.count("A")
t[1] = s.count("B")
t[2] = s.count("C")
t[3] = s.count("D")
t[4] = s.count("E")
t[5] = s.count("F")

print(" ".join(map(str,t)))
