from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visit = [[-1] * w for _ in range(h)]
  visit[x][y] = 0
  cnt = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == -1:
        if graph[nx][ny] == 'L':
          q.append((nx, ny))
          visit[nx][ny] = visit[x][y] + 1
          cnt = max(visit[nx][ny], cnt)

  return cnt
  
h, w = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
res = 0

for i in range(h):
  for j in range(w):
    if graph[i][j] == 'L':
      res = max(res, bfs(i, j))

print(res)