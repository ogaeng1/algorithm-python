T = int(input())

for _ in range(T):
  n, str = input().split()
  n = int(n)
  print(str[:n-1] + str[n:])