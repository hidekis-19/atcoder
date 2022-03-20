N = int(input())
S = list(input())
S_W = S.count('W')
S_R = S.count('R')
if S_W == len(S) or S_W == 0:
  print(0)
else:
  ans = 0
  for i in range(S_R):
    if S[i] == 'W':
      ans = ans + 1
  print(ans)