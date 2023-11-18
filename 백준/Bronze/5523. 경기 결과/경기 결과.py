import sys
N = int(sys.stdin.readline())
A, B = 0, 0

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  if a > b:
    A += 1
  elif a < b:
    B += 1

print(A, B)