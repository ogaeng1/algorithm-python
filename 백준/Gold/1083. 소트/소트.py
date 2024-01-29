from sys import stdin

n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
s = int(stdin.readline())

for i in range(n):
  idx = i
  for j in range(i + 1, min(n, i+1+s)):
      if A[j] > A[idx]:
          idx = j

  for k in range(idx, i, -1):
      A[k], A[k - 1] = A[k - 1], A[k]
      s -= 1

  if s == 0:
      break

print(*A)