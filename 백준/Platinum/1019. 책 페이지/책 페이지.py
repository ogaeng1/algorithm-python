import sys
input = sys.stdin.readline

n = int(input())
page = [0] * 10
num = 1

def convert(n):
  while n % 10 != 9:
    for i in str(n):
      page[int(i)] += num
    n -= 1
  return n

while n > 0:
  n = convert(n)
  if n < 10:
    for i in range(n+1):
      page[i] += num
  else:
    for i in range(10):
      page[i] += (n // 10+1)*num
  page[0] -= num
  num *= 10
  n //= 10

for i in range(10):
  print(page[i], end=' ')