def kaprekar(n):
  n = n + sum(map(int, str(n)))
  return n

arr = []

for i in range(1, 10001):
  arr.append(kaprekar(i))

for i in range(1, 10001):
  if i not in arr:
    print(i)