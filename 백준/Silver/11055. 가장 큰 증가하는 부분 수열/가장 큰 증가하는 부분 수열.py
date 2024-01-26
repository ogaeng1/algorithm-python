n = int(input())
A = list(map(int, input().split()))

dp = A[:]

for i in range(n):
  for j in range(i):
    if A[i] > A[j] and dp[i] < A[i] + dp[j]:
      dp[i] = dp[j] + A[i]

print(max(dp))