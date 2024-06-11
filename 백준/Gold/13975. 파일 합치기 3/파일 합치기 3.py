import sys, heapq
input = sys.stdin.readline


T = int(input())
for _ in range(T):
  heap = []
  K = int(input())
  file = list(map(int, input().split()))
  res = 0

  for i in file:
    heapq.heappush(heap, i)

  while len(heap) > 1:
    add_file = 0
    f1 = heapq.heappop(heap)
    f2 = heapq.heappop(heap)

    add_file += f1 + f2
    res += add_file
    heapq.heappush(heap, add_file)

  print(res)