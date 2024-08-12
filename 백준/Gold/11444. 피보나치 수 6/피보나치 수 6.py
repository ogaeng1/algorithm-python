import sys
input = sys.stdin.readline

MOD = 1000000007

def fibonacci(n):
  if n == 0:
    return (0, 1)
  else:
    a, b = fibonacci(n // 2)
    c = a * ((2 * b) - a)
    d = a * a + b * b
    if n % 2 == 0:
      return (c % MOD, d % MOD)
    else:
      return (d % MOD, (c + d) % MOD)

n = int(input())
res, _ = fibonacci(n)
print(res)