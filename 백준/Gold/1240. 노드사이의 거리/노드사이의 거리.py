import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(u, v, d):
  visit[u] = True
  if u == v:
    return d

  for x, y in graph[u]:
    if visit[x]:
      continue
    
    res = dfs(x, v, d+y)
    if res:
      return res
  return 0

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  u, v, cost = map(int, input().split())
  graph[u].append([v, cost])
  graph[v].append([u, cost])

for _ in range(m):
  u, v = map(int, input().split())
  visit = [False] * (n+1)
  print(dfs(u, v, 0))