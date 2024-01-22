from sys import stdin

n = int(stdin.readline())
day, money = [], []
dp = [0] * (n+1)
result = 0

for _ in range(n):
  t, p = map(int, stdin.readline().split())
  day.append(t)
  money.append(p)

for i in range(n-1, -1, -1):
  if day[i] + i <= n:
    dp[i] = max(money[i] + dp[day[i]+i], result)
    result = dp[i]
  else:
    dp[i] = result

print(result)