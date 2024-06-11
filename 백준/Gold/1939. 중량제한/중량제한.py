import sys
from collections import deque
input = sys.stdin.readline

def bfs(visit, mid):
  visit[start] = 1
  q = deque()
  q.append(start)

  while q:
    cur = q.popleft()
    if cur == end:
      return True
    for i, j in graph[cur]:
      if visit[i] == 0 and mid <= j:
        q.append(i)
        visit[i] = 1

  return False

def binary_search():
  min_weight, max_weight = 1, 1000000000
  while min_weight <= max_weight:
    visit = [0 for _ in range(n+1)]
    mid = (min_weight + max_weight) // 2
  
    if bfs(visit, mid):
      min_weight = mid + 1
    else:
      max_weight = mid - 1

  return max_weight
    
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

start, end = map(int, input().split())
print(binary_search())