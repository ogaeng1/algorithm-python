import sys

n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

start, end = 0, max(price)

while start <= end:
  mid = (start + end) // 2
  res = 0

  for i in price:
    if i <= mid:
      res += i
    else:
      res += mid

  if res <= total:
    start = mid + 1
  else:
    end = mid - 1

print(end)