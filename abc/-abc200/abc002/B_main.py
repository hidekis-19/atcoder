w = input()

t = ""

for ww in list(w):
    if ww == "a" or ww == "i" or ww == "u" or ww == "e" or ww == "o":
        continue
    else:
        t = t + ww
print(t)