def backtracking():
  if len(res) == M:
    print(*res)

  for i in range(1, N+1):
    if i not in res and len(res) == 0 or i > res[-1]:
      res.append(i)
      backtracking()
      res.pop()

N, M = map(int, input().split())
res = []

backtracking()