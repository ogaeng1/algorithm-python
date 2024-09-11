import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

com1 = []
for i in A:
  for j in B:
    com1.append(i+j)
com1.sort()

com2 = []
for i in C:
  for j in D:
    com2.append(i+j)
com2.sort()

res = total = 0
left, right = 0, len(com2)-1
while 0 <= right and left < len(com1):
  total = com1[left] + com2[right]
  if total < 0:
    left += 1
  elif total > 0:
    right -= 1
  else:
    x = 1
    for i in range(left+1, len(com1)):
      if com1[left] == com1[i]:
        x += 1
      else:
        break
    y = 1
    for i in range(right-1, -1, -1):
      if com2[right] == com2[i]:
        y += 1
      else:
        break
    res += x*y
    left += x
    right -= y

print(res)
