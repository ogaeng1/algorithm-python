import heapq, sys
input = sys.stdin.readline

min_heap = []
max_heap = []
N = int(input())
for _ in range(N):
  num = int(input())

  if len(min_heap) == len(max_heap):
    heapq.heappush(max_heap, -num)
  else:
    heapq.heappush(min_heap, num)

  if min_heap and -max_heap[0] > min_heap[0]:
    max_val = -heapq.heappop(max_heap)
    min_val = heapq.heappop(min_heap)

    heapq.heappush(max_heap, -min_val)
    heapq.heappush(min_heap, max_val)

  print(-max_heap[0])