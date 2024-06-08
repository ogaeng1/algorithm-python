import sys, heapq
input = sys.stdin.readline

heap = []
n, h, t = map(int, input().split())

for _ in range(n):
  height = int(input())
  heapq.heappush(heap, -height)

res = 0
use_hammer = 0
while t > 0 and -heap[0] >= h:
  tallest_giant = -heapq.heappop(heap)

  if tallest_giant == 1:
    heapq.heappush(heap, -tallest_giant)
    break
  max_height = max(1, tallest_giant // 2)
  heapq.heappush(heap, -max_height)
  use_hammer += 1
  t -= 1

if -heap[0] < h:
  print('YES')
  print(use_hammer)
else:
  print('NO')
  print(-heap[0])