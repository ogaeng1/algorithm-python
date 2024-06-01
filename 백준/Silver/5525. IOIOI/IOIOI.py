import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

l, r = 0, 0
res = 0

while r < M:
  if S[r:r+3] == 'IOI':
    r += 2
    if r - l == N*2:
      l += 2
      res += 1
  else:
    l = r + 1
    r += 1

print(res)