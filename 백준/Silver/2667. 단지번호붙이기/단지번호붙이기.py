def dfs(x, y):
  visit[x][y] = True
  cnt = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == '1' and not visit[nx][ny]:
      cnt += dfs(nx, ny)

  return cnt
  
N = int(input())

graph = [list(input()) for _ in range(N)]
visit = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

complex = []

for i in range(N):
  for j in range(N):
    if graph[i][j] == '1' and not visit[i][j]:
      complex.append(dfs(i, j))

print(len(complex))
for i in sorted(complex):
  print(i)