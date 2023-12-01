n = int(input())
res = 0

for i in range(1, n+1):
  num = list(map(int, str(i)))
  res = sum(num) + i

  if res == n:
    print(i)
    break
  elif i == n:
    print(0)