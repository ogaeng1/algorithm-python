import sys

N = list(map(int, (sys.stdin.readline().split())))
cnt = 0

for i in range(len(N)):
  if N[i] > 0:
    cnt += 1
  else:
    continue

print(cnt)