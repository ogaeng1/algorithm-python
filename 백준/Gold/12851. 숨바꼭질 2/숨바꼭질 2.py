import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([N])

visit = [-1] * 100001
visit[N] = 0

cnt = 0
min_time = float('inf')

while q:
  x = q.popleft()
  if x == K:
    if visit[x] < min_time:
      min_time = visit[x]
      cnt = 1
    elif visit[x] == min_time:
      cnt += 1
    continue
    
  for nx in (x - 1, x + 1, 2 * x):
      if 0 <= nx <= 100000:
        if visit[nx] == -1 or visit[nx] == visit[x] + 1:
          visit[nx] = visit[x] + 1
          q.append(nx)

print(min_time)
print(cnt)