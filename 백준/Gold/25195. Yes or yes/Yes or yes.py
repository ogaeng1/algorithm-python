import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(v):
  visit[v] = True
  is_meet_fan = not graph[v]
  for i in graph[v]:
    if not visit[i] and dfs(i):
      return True
  return is_meet_fan
  
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  
s = int(input())
fan_club = list(map(int, input().split()))
for i in fan_club:
  visit[i] = True

print('Yes' if visit[1] or not dfs(1) else 'yes')