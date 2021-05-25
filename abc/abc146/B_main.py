n = int(input())
S = input()

x = ''
for s in S:
     a = ord(s)
     y = a+n
     if y >90:
         y = y -26 
     b = chr(y) 
     x = x+b
print(x)