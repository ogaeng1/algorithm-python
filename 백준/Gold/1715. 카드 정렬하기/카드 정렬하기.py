import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
  num = int(sys.stdin.readline())
  heapq.heappush(heap, num)

heap.sort()
res = 0

while len(heap) > 1:
  card1 = heapq.heappop(heap)
  card2 = heapq.heappop(heap)
  res += (card1 + card2)
  heapq.heappush(heap, card1+card2)

print(res)