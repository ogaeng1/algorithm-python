n = int(input())
d = [0] * 91

def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  if d[n] != 0:
    return d[n]

  d[n] = fibonacci(n-1) + fibonacci(n-2)
  return d[n]

print(fibonacci(n))