import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, y, h):
  visit[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N:
      if zone[nx][ny] > h and not visit[nx][ny]:
        dfs(nx, ny, h)

N = int(input())

zone = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
max_num = []

for i in zone:
  max_num.append(max(i))

biggest = max(max_num)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe_zone = 0

for h in range(biggest+1):
  safe = 0
  visit = [[False] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if zone[i][j] > h and not visit[i][j]:
        dfs(i, j, h)
        safe += 1

  safe_zone = max(safe_zone, safe)

print(safe_zone)