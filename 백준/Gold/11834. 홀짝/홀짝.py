import sys
input = sys.stdin.readline

n = int(input())

x = 10**100
y = 0
while x > y:
  b = (x+y) // 2
  if b*b + b >= 2*n:
    x = b - 1
  elif b*b + 3*b + 2 < 2*n:
    y = b + 1
  else:
    x = b
    break

x += 1
res = 2*n - x
print(res)