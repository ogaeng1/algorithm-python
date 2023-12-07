import sys
input = sys.stdin.readline

def numRound(num):
  return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
avg = numRound(n * 0.15)

level_list = [int(input()) for _ in range(n)]
level_list.sort()

if n == 0:
  print(0)
else:
  res = 0
  for i in range(avg, n-avg):
    res += level_list[i]
  res = res / (n-2*avg)
  print(numRound(res))