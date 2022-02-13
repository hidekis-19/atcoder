s = input()

s_len = len(s)

cnt_end =0
cnt_start =0
for l in range(s_len):
    if s[s_len - l -1] == "a":
        cnt_end += 1
    else:
        break

for l in range(s_len):
    if s[l] == "a":
        cnt_start += 1
    else:
        break

aa = ""
if cnt_end >= cnt_start:
    aa = "a"* (cnt_end-cnt_start)
else:
    print("No")
    exit()

u = aa + s


if str(u) == str(u)[::-1]:
    print("Yes")
    exit()
else:
    print("No")


    

    