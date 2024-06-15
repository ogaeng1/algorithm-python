import sys
input = sys.stdin.readline
n = int(input())

wire = []
dp = [1] * n
for _ in range(n):
  a, b = map(int, input().split())
  wire.append((a, b))

wire.sort()

for i in range(1, n):
  for j in range(i):
    if wire[i][1] > wire[j][1]:
      dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))