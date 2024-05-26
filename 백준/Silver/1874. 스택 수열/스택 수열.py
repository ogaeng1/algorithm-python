import sys

n = int(sys.stdin.readline().strip())

res, stack = [], []
cur = 1

for _ in range(n):
  num = int(sys.stdin.readline().strip())

  while cur <= num:
    stack.append(cur)
    res.append('+')
    cur += 1

  if stack[-1] == num:
    stack.pop()
    res.append('-')
  else:
    res.clear()
    res.append('NO')
    break

for i in res:
  print(i)