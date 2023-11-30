a, b, c, d, e, f = map(int, input().split())
x, y = 0, 0

for i in range(-999, 1000, 1):
  for j in range(-999, 1000, 1):
    if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
      x = i
      y = j
      break
    else:
      continue

print(x, y)