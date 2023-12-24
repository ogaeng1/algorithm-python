n, m = map(int, input().split())

if n == 0:
  print(0)
else:
  weight = list(map(int, input().split()))
  res, cnt = 0, 0

  for i in weight:
    res += i
    if res > m:
      cnt += 1
      res = i
    elif res == m:
      cnt += 1
      res = 0
  if res > 0:
    cnt += 1
  print(cnt)