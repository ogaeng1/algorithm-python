n, k = map(int, input().split())
coins = []

for _ in range(n):
  coin = int(input())
  if coin <= k:
    coins.append(coin)

if len(coins) == 0:
  print(0)
else:
  dp = [0] * k
  for i in range(len(coins)):
    dp[coins[i]-1] += 1
    for j in range(coins[i], k):
      dp[j] += dp[j - coins[i]]
  print(dp[k-1])