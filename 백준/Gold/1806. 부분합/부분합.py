import sys
input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))

start = end = acc = 0
min_len = float('inf')

while end < n:
  acc += seq[end]
  end += 1

  while acc >= s:
    min_len = min(min_len, end-start)
    acc -= seq[start]
    start += 1

print(0 if min_len == float('inf') else min_len)