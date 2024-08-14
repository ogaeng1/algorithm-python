import sys
input = sys.stdin.readline

def backtracking(x):
  if x == m:
    print(' '.join(map(str, res)))
    return

  for i in range(n):
    if num[i] in res:
      continue
    res.append(num[i])
    backtracking(x+1)
    res.pop()

n, m = map(int, input().split())
num = [int(i) for i in input().split()]
num.sort()
res = []
backtracking(0)