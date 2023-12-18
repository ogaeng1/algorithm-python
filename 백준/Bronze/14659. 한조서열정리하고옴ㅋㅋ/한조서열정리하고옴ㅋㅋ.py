n = int(input())
peak = list(map(int, input().split()))

max_high = 0
kill = 0
res = 0

for i in peak:
  if i > max_high:
    max_high = i
    kill = 0

  if i < max_high:
    kill += 1
  res = max(res, kill)

print(res)