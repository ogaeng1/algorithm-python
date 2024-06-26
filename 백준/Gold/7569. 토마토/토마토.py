from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  while q:
    z, x, y = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0:
        graph[nz][nx][ny] = graph[z][x][y] + 1
        q.append((nz, nx, ny))

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for z in range(H):
  for x in range(N):
    for y in range(M):
      if graph[z][x][y] == 1:
        q.append((z, x, y))
    
bfs()
res = 0
for z in range(H):
  for x in range(N):
    for y in range(M):
      if graph[z][x][y] == 0:
        print(-1)
        exit(0)
      res = max(res, graph[z][x][y])

print(res-1)