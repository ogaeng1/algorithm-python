import sys
input = sys.stdin.readline

def dfs(x):
  if len(res) == m:
    print(*res)
    return

  for i in range(x, n+1):
    res.append(i)
    dfs(i)
    res.pop()

n, m = map(int, input().split())
res = []
dfs(1)