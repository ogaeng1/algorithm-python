computer = int(input())
pair = int(input())

graph = [[] for _ in range(computer+1)]

for _ in range(pair):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visit = [0] * (computer+1)

def dfs(v):
  visit[v] = 1

  for i in graph[v]:
    if visit[i] == 0:
      dfs(i)

dfs(1)
print(sum(visit)-1)