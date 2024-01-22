n = int(input())
A = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
  for j in range(i):
    if A[j] < A[i]:
      dp[i] = max(dp[i], dp[j]+1)

length = max(dp)
result_A = []

for i in range(n-1, -1, -1):
  if dp[i] == length:
    result_A.append(A[i])
    length -= 1

result_A.reverse()

print(max(dp))
print(*result_A)