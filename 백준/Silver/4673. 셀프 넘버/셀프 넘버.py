def kaprekar(n):
  n = n + sum(map(int, str(n)))
  return n

num = set()

for i in range(1, 10001):
  num.add(kaprekar(i))

for i in range(1, 10001):
  if i not in num:
    print(i)