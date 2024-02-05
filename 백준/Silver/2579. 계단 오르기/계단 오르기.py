n = int(input())

score = [0] * 301
dp = [0] * 301

for i in range(1, n+1):
  x = int(input())
  score[i] = x

dp[1] = score[1]
dp[2] = score[1] + score[2]
dp[3] = max(score[1] + score[3], score[2] + score[3])

for i in range(4, n+1):
  dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])

print(dp[n])