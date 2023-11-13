import sys
from collections import deque

q = deque([])
n = int(input())

for _ in range(n):
  word = sys.stdin.readline().split()
  
  if word[0] == "push":
    q.append(word[1])
  elif word[0] == "pop":
    if len(q) == 0:
      print(-1)
    else:
      print(q.popleft())
  elif word[0] == "size":
    print(len(q))
  elif word[0] == "empty":
    if len(q) == 0:
      print(1)
    else:
      print(0)
  elif word[0] == "front":
    if len(q) == 0:
      print(-1)
    else:
      print(q[0])
  elif word[0] == "back":
    if len(q) == 0:
      print(-1)
    else:
      print(q[-1])