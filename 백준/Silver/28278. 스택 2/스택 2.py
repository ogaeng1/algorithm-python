from collections import deque
import sys
q = deque()

n = int(sys.stdin.readline())

for _ in range(n):
  num = sys.stdin.readline().split()
  if num[0] == '1':
    q.append(num[1])
  elif num[0] == '2':
    if q:
      print(q[-1])
      q.pop()
    else:
      print(-1)
  elif num[0] == '3':
    print(len(q))
  elif num[0] == '4':
    if q:
      print(0)
    else:
      print(1)
  elif num[0] == '5':
    if q:
      print(q[-1])
    else:
      print(-1)