import sys
from collections import deque
d = deque()

N = int(input())

for _ in range(N):
  data = list(map(int, sys.stdin.readline().split()))
  if data[0] == 1:
    d.appendleft(data[1])
  elif data[0] == 2:
    d.append(data[1])
  elif data[0] == 3:
    if len(d) == 0:
      print(-1)
    else:
      print(d[0])
      d.popleft()
  elif data[0] == 4:
    if len(d) == 0:
      print(-1)
    else:
      print(d[-1])
      d.pop()
  elif data[0] == 5:
    print(len(d))
  elif data[0] == 6:
    if len(d) == 0:
      print(1)
    else:
      print(0)
  elif data[0] == 7:
    if len(d) == 0:
      print(-1)
    else:
      print(d[0])
  elif data[0] == 8:
    if len(d) == 0:
      print(-1)
    else:
      print(d[-1])