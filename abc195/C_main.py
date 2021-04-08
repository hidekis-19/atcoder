import math
num=  input()
len_num = len(num)
num = int(num)


if len_num <=3:
    ans = 0
elif len_num <=6:
    ans = num - 999
elif len_num <=9:
    ans = (num -999999) *2 + 999000 
elif len_num <=12:
    ans = (num -999999999) *3 + 999000000 *2 + 999000
elif len_num <=15:
    ans = (num -999999999999) *4 + 999000000000*3 + 999000000 *2 + 999000



print(ans)
