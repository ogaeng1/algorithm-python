import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []

init = list(map(int, input().split()))
for i in init:
  heapq.heappush(heap, i)

for _ in range(N-1):
  num_list = list(map(int, input().split()))

  for j in num_list:
    if heap[0] < j:
      heapq.heappush(heap, j)
      heapq.heappop(heap)

print(heap[0])