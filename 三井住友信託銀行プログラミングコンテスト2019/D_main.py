import itertools
N = int(input())
S = input()

x = len(S)  -(N -3)

S_l = list(S)


c_list = list(itertools.combinations(S_l, x))

print(len(set(c_list)))

