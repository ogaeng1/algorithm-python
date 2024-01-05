from sys import stdin

n, m = map(int, stdin.readline().split())
timer = [int(stdin.readline()) for _ in range(n)]

start, end = min(timer), max(timer) * m
res = 0

while start <= end:
  mid = (start + end) // 2
  cnt = 0

  for i in range(n):
    cnt += mid // timer[i]

  if cnt >= m:
    end = mid - 1
    res = mid
  else:
    start = mid + 1

print(res)