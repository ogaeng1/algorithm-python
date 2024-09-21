import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []

for _ in range(n):
  coin.append(int(input()))

dp = [float('inf')] * (k+1)
dp[0] = 0

for i in coin:
  for j in range(i, k+1):
    dp[j] = min(dp[j], dp[j-i]+1)

print(-1 if dp[k] == float('inf') else dp[k])