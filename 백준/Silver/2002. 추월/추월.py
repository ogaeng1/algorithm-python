import sys
input = sys.stdin.readline

N = int(input())
in_tunnel = {input(): i for i in range(N)}
out_tunnel = [input() for _ in range(N)]

cnt = 0

for i in range(N-1):
  cur_in = in_tunnel[out_tunnel[i]]
  for j in range(i+1, N):
    next_in = in_tunnel[out_tunnel[j]]
    if next_in < cur_in:
      cnt += 1
      break

print(cnt)