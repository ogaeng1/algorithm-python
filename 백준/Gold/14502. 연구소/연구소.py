import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
arr = [[0] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
  maps.append(list(map(int, input().split())))

res = 0

def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and nx < N and ny >= 0 and ny < M:
      if arr[nx][ny] == 0:
        arr[nx][ny] = 2
        virus(nx, ny)

def safe_zone():
  safe = 0
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 0:
        safe += 1
  return safe

def dfs(cnt):
  global res
  if cnt == 3:
    for i in range(N):
      for j in range(M):
        arr[i][j] = maps[i][j]

    for i in range(N):
      for j in range(M):
        if arr[i][j] == 2:
          virus(i, j)

    res = max(res, safe_zone())
    return

  for i in range(N):
    for j in range(M):
      if maps[i][j] == 0:
        maps[i][j] = 1
        cnt += 1
        dfs(cnt)
        maps[i][j] = 0
        cnt -= 1
  
dfs(0)
print(res)