import sys
from collections import defaultdict
input = sys.stdin.readline
test_case = 1

def dfs(graph, v, visit):
  visit[v] = True

  for i in graph[v]:
    if not visit[i]:
      dfs(graph, i, visit)

while True:
  N = int(input())

  if N == 0:
    break

  maniddo_order = defaultdict(int)
  maniddo_list = []
  graph = [[] for _ in range(N+1)]
  visit = [False] * (N+1)
  num = 1
  res = 0
  
  for _ in range(1, N+1):
    maniddo = input().split()
    maniddo_list.append([maniddo[0], maniddo[1]])
    if maniddo[0] not in maniddo_order:
      maniddo_order[maniddo[0]] = num
      num += 1
    if maniddo[1] not in maniddo_order:
      maniddo_order[maniddo[1]] = num
      num += 1

  for give, take in maniddo_list:
    g = maniddo_order.get(give)
    t = maniddo_order.get(take)
    graph[g].append(t)
  
  for i in range(1, N+1):
    if not visit[i]:
      dfs(graph, i ,visit)
      res += 1

  print(test_case, res)
  test_case += 1