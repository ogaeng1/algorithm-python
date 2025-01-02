import sys
input = sys.stdin.readline

def divide(a, b, c):
  if b == 0:
    return 1

  n = divide(a, b // 2, c)
  n = (n * n) % c

  if b % 2 == 1:
    n = (n * a) % c
  return n

a, b, c = map(int, input().split())

print(divide(a, b, c))