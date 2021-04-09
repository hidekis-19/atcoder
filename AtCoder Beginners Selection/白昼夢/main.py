S = input()
T = ['dream' ,'dreamer' ,'erase' ,'eraser']
ans = []

def str_replace(str_1,str_2):
    if str_2 in str_1:
        str_3 = str_1.replace(str_2,'')
        return str_3
    return str_1

S1 = str_replace(S,T[0])
S1 = str_replace(S1,T[1])
S1 = str_replace(S1,T[2])
S1 = str_replace(S1,T[3])
ans.append(S1)


S2 = str_replace(S,T[0])
S2 = str_replace(S2,T[1])
S2 = str_replace(S2,T[3])
S2 = str_replace(S2,T[2])
ans.append(S2)

S3 = str_replace(S,T[0])
S3 = str_replace(S3,T[2])
S3 = str_replace(S3,T[1])
S3 = str_replace(S3,T[3])
ans.append(S3)


S4 = str_replace(S,T[0])
S4 = str_replace(S4,T[2])
S4 = str_replace(S4,T[3])
S4 = str_replace(S4,T[1])
ans.append(S4)

S5 = str_replace(S,T[0])
S5 = str_replace(S5,T[3])
S5 = str_replace(S5,T[1])
S5 = str_replace(S5,T[2])
ans.append(S5)

S6 = str_replace(S,T[0])
S6 = str_replace(S6,T[3])
S6 = str_replace(S6,T[2])
S6 = str_replace(S6,T[1])
ans.append(S6)

S7 = str_replace(S,T[1])
S7 = str_replace(S7,T[0])
S7 = str_replace(S7,T[2])
S7 = str_replace(S7,T[3])
ans.append(S7)

S8 = str_replace(S,T[1])
S8 = str_replace(S8,T[0])
S8 = str_replace(S8,T[3])
S8 = str_replace(S8,T[2])
ans.append(S8)

S9 = str_replace(S,T[1])
S9 = str_replace(S9,T[2])
S9 = str_replace(S9,T[0])
S9 = str_replace(S9,T[3])
ans.append(S9)

S10 = str_replace(S,T[1])
S10 = str_replace(S10,T[2])
S10 = str_replace(S10,T[3])
S10 = str_replace(S10,T[0])
ans.append(S10)

S11 = str_replace(S,T[1])
S11 = str_replace(S11,T[3])
S11 = str_replace(S11,T[0])
S11 = str_replace(S11,T[2])
ans.append(S11)

S12 = str_replace(S,T[1])
S12 = str_replace(S12,T[3])
S12 = str_replace(S12,T[2])
S12 = str_replace(S12,T[0])
ans.append(S12)

S13 = str_replace(S,T[2])
S13 = str_replace(S13,T[0])
S13 = str_replace(S13,T[1])
S13 = str_replace(S13,T[3])
ans.append(S13)

S14 = str_replace(S,T[2])
S14 = str_replace(S14,T[0])
S14 = str_replace(S14,T[3])
S14 = str_replace(S14,T[1])
ans.append(S14)

S15 = str_replace(S,T[2])
S15 = str_replace(S15,T[1])
S15 = str_replace(S15,T[0])
S15 = str_replace(S15,T[3])
ans.append(S15)

S16 = str_replace(S,T[2])
S16 = str_replace(S16,T[1])
S16 = str_replace(S16,T[3])
S16 = str_replace(S16,T[0])
ans.append(S16)

S17 = str_replace(S,T[2])
S17 = str_replace(S17,T[3])
S17 = str_replace(S17,T[0])
S17 = str_replace(S17,T[1])
ans.append(S17)

S18 = str_replace(S,T[2])
S18 = str_replace(S18,T[3])
S18 = str_replace(S18,T[1])
S18 = str_replace(S18,T[0])
ans.append(S18)

S19 = str_replace(S,T[3])
S19 = str_replace(S19,T[0])
S19 = str_replace(S19,T[1])
S19 = str_replace(S19,T[2])
ans.append(S19)

S20 = str_replace(S,T[3])
S20 = str_replace(S20,T[0])
S20 = str_replace(S20,T[2])
S20 = str_replace(S20,T[1])
ans.append(S20)

S21 = str_replace(S,T[3])
S21 = str_replace(S21,T[1])
S21 = str_replace(S21,T[0])
S21 = str_replace(S21,T[2])
ans.append(S21)

S22 = str_replace(S,T[3])
S22 = str_replace(S22,T[1])
S22 = str_replace(S22,T[2])
S22 = str_replace(S22,T[0])
ans.append(S22)

S23 = str_replace(S,T[3])
S23 = str_replace(S23,T[2])
S23 = str_replace(S23,T[0])
S23 = str_replace(S23,T[1])
ans.append(S23)

S24 = str_replace(S,T[3])
S24 = str_replace(S24,T[2])
S24 = str_replace(S24,T[1])
S24 = str_replace(S24,T[0])
ans.append(S24)


if (len(S1) == 0) or (len(S2) == 0) or (len(S2) == 0) or (len(S4) == 0) \
    or (len(S5) == 0) or (len(S6) == 0) or (len(S7) == 0) or (len(S8) == 0) \
    or (len(S9) == 0) or (len(S10) == 0) or (len(S11) == 0) or (len(S12) == 0) \
    or (len(S13) == 0) or (len(S14) == 0) or (len(S15) == 0) or (len(S16) == 0) \
    or (len(S17) == 0) or (len(S18) == 0) or (len(S19) == 0) or (len(S20) == 0) \
    or (len(S21) == 0) or (len(S22) == 0) or (len(S23) == 0) or (len(S24) == 0):
    ans = 'YES'
else:
    ans = 'NO'
    
print(ans)