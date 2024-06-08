import sys, math
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  bridge = int(input())
  max_bridge = int((-1 + math.sqrt(1 + 8*bridge)) // 2)
  print(max_bridge)