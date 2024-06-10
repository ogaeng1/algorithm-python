import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(v):
  global cnt
  visit[v] = True
  for i in graph[v]:
    if not visit[i]:
      cnt += 1
      dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for i in range(m):
  x, y = map(int, input().split())
  graph[y].append(x)
x = int(input())

cnt = 0
dfs(x)

print(cnt)