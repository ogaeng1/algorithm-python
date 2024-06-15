import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
  coin = int(input())
  coins = list(map(int, input().split()))
  price = int(input())

  dp = [0] * (price+1)
  dp[0] = 1
  
  for i in coins:
    for j in range(price+1):
      if j >= i:
        dp[j] += dp[j-i]

  print(dp[price])