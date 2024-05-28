import sys
sys.setrecursionlimit(1000000)

def dfs(graph, v, visit):
  visit[v] = True

  for i in graph[v]:
    if not visit[i]:
      dfs(graph, i, visit)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())

  graph[u].append(v)
  graph[v].append(u)

cnt = 0

for i in range(1, N+1):
  if not visit[i]:
    dfs(graph, i, visit)
    cnt += 1

print(cnt)