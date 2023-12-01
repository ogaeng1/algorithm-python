n, m = map(int, input().split())

res1, res2 = '', ''

for _ in range(n):
  for i in input().rstrip():
    res1 += i*2

for _ in range(n):
  res2 += input().rstrip()

print('Eyfa' if res1 == res2 else 'Not Eyfa')