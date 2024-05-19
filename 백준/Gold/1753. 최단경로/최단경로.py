import heapq
import sys

def dijkstra(s):
  q = []
  heapq.heappush(q, (0, s))
  dis[s] = 0

  while q:
    dist, now = heapq.heappop(q)

    if dis[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < dis[i[0]]:
        dis[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())
s = int(input())

graph = [[] for i in range(V+1)]
dis = [INF] * (V + 1)

for _ in range(E):
  u, v, w = map(int, input().split())

  graph[u].append((v, w))

dijkstra(s)

for i in range(1, V+1):
  if dis[i] == INF:
    print('INF')
  else:
    print(dis[i])