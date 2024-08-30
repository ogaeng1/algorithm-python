import sys
input = sys.stdin.readline

def dfs(x, y):
  res = 1

  for i in range(4):
    nx = x + dx[i] 
    ny = y + dy[i]
    
    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in visit:
      visit.add(graph[nx][ny])
      res = max(res, dfs(nx, ny) + 1)
      visit.remove(graph[nx][ny])

  return res

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visit = set()
visit.add(graph[0][0])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(dfs(0, 0))