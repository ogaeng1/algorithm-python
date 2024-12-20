import sys
input = sys.stdin.readline

N=int(input())
rgb=[list(map(int,input().split())) for _ in range(N)]
res = inf = 10000000

for i in range(3):
  dp = [[inf, inf, inf] for _ in range(N)]
  dp[0][i] = rgb[0][i]
  for j in range(1, N):
    dp[j][0] = rgb[j][0] + min(dp[j-1][1],dp[j-1][2])
    dp[j][1] = rgb[j][1] + min(dp[j-1][0],dp[j-1][2])
    dp[j][2] = rgb[j][2] + min(dp[j-1][0],dp[j-1][1])
  for k in range(3):
    if i != k:
      res=min(res,dp[-1][k])
      
print(res)