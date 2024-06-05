import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  gwal_ho = input().strip()
  res = 0

  for i in gwal_ho:
    if i == '(':
      res += 1
    else:
      res -= 1
      
    if res < 0:
      break

  print('YES' if res == 0 else 'NO')