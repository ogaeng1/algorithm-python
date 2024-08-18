from collections import deque

def bfs(n, edge):
  start_node = [0] * (n+1)
  graph = [[] for _ in range(n+1)]

  for x, y in edge:
    graph[x].append(y)
    start_node[y] += 1

  q = deque([i for i in range(1, n+1) if start_node[i] == 0])
  result = []

  while q:
    node = q.popleft()
    result.append(node)
    for n in graph[node]:
      start_node[n] -= 1
      if start_node[n] == 0:
        q.append(n)

  return result

n, m = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(m)]
res = bfs(n, edge)

print(" ".join(map(str, res)))