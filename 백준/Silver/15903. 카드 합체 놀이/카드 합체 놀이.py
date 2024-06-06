import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
heap = []

for i in card:
  heapq.heappush(heap, i)

for _ in range(m):
  x = heapq.heappop(heap)
  y = heapq.heappop(heap)
  new_card = x + y

  heapq.heappush(heap, new_card)
  heapq.heappush(heap, new_card)

print(sum(heap))