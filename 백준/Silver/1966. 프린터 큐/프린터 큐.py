import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().strip().split())
  doc = deque(map(int, input().strip().split()))

  res = 1
  while doc:
    if doc[0] < max(doc):
      doc.append(doc.popleft())

    else:
      if m == 0: 
        break
      doc.popleft()
      res += 1

    m = m - 1 if m > 0 else len(doc) - 1

  print(res)