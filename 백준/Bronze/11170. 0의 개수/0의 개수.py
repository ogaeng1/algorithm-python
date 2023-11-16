T = int(input())

for i in range(T):
  a, b = map(int, input().split())
  cnt = 0
  for i in range(a, b+1):
    cnt += str(i).count("0")
  print(cnt)