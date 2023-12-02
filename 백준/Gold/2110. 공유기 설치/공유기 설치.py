import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lan = []

for _ in range(n):
  lan.append(int(input()))
lan.sort()

start, end = 1, lan[-1] - lan[0]
res = 0

while start <= end:
  mid = (start + end) // 2
  prev = lan[0]
  cnt = 1

  for i in range(1, n):
    if lan[i] >= prev + mid:
      cnt += 1
      prev = lan[i]

  if cnt >= c:
    start = mid + 1
    res = mid
  else:
    end = mid - 1

print(res)