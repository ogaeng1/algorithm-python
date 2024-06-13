import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  while q:
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 0:
          q.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1

  return
      

N, M = map(int, input().split())
graph = []
q = deque()

for i in range(N):
  sq = list(map(int, input().split()))
  for j in range(M):
    if sq[j] == 1:
      q.append((i, j))
  graph.append(sq)


dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      q.append((i, j))
      graph[i][j] = 1  

safe = 0
bfs()

for i in range(N):
  for j in range(M):
    safe = max(safe, graph[i][j])

print(safe-1)