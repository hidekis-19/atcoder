A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for i in range(A+1):
    if (500*i) > X:
        break
    elif (500*i) == X:
        ans += 1
    else:
        X_B = X -(500*i)
        for j in range(B+1):
            if (100*j) > X_B:
                break
            elif (100*j) == X_B:
                ans += 1
            else:
                X_C = X_B - (100*j)
                for k in range(C+1):
                    if (50*k) > X_C:
                        break
                    elif (50*k) == X_C:
                        ans += 1

print(ans)