import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
time = sorted(list(map(int, input().split())), reverse=True)
heap = []

for i in time:
  if len(heap) < m:
    heapq.heappush(heap, i)
  else:
    heapq.heappush(heap, i+heapq.heappop(heap))

print(max(heap))