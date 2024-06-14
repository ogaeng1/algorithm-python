import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(n, start, graph):
  dist = [INF] * (n + 1)
  dist[start] = 0
  q = [(0, start)]

  while q:
    cur, node = heapq.heappop(q)

    if cur > dist[node]:
        continue

    for i, j in graph[node]:
      time = cur + i
      if time < dist[j]:
        dist[j] = time
        heapq.heappush(q, (time, j))

  return dist

t = int(input())
res = []

for _ in range(t):
  n, d, c = map(int, input().split())
  graph = [[] for _ in range(n + 1)]

  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((s, a))

  dist = dijkstra(n, c, graph)
  virus = time = 0

  for i in dist:
    if i != INF:
      virus += 1
      if i > time:
        time = i

  res.append((virus, time))

for i in res:
  print(i[0], i[1])