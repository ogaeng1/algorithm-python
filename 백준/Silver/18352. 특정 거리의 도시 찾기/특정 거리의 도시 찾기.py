import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0 
dq = deque([x])


for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)

while dq:
  cur = dq.popleft()
  for i in graph[cur]:
    if distance[i] == -1:
      distance[i] = distance[cur] + 1
      dq.append(i)

visit = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    visit = True
    
if not visit:
  print(-1)