import sys
input = sys.stdin.readline

n = int(input())
angry = []
for _ in range(n):
  angry.append(int(input()))

angry.sort()
res = 0

for i in range(1, n+1):
  res += abs(i-angry[i-1])
print(res)