a,b,c,d= map(int, input().split())

x = 60 * a + b
y = 60 * c + d
if x <= y:
    print("Takahashi")
else:
    print("Aoki")
