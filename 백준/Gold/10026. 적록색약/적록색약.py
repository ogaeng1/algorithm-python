import sys
sys.setrecursionlimit(100000)

def dfs(x, y, graph, visit):
  visit[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and graph[x][y] == graph[nx][ny]:
      dfs(nx, ny, graph, visit)
    
N = int(input())

graph = [list(input()) for _ in range(N)]
visit_normal = [[False] * N for _ in range(N)]
visit_abnormal = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

normal, abnormal = 0, 0

# 적록색약 아닌 사람이 보는 그림
for i in range(N):
  for j in range(N):
    if not visit_normal[i][j]:
      dfs(i, j, graph, visit_normal)
      normal += 1

# 적록색약인 사람이 보는 그림
for i in range(N):
  for j in range(N):
    if graph[i][j] == 'R':
      graph[i][j] = 'G'

for i in range(N):
  for j in range(N):
    if not visit_abnormal[i][j]:
      dfs(i, j, graph, visit_abnormal)
      abnormal += 1

print(normal, abnormal)