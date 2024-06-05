import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
position = list(map(int, input().split()))
cnt = 0

dq = deque(i for i in range(1, N+1))

for i in position:
  dq_len = len(dq)
  
  while True:
    if dq[0] == i:
      dq.popleft()
      break
    else:
      if dq.index(i) <= dq_len // 2:
        dq.rotate(-1)
        cnt += 1
      else:
        dq.rotate(1)
        cnt += 1

print(cnt)