import sys, heapq
input = sys.stdin.readline

dasom = 0
heap = []
n = int(input())
for i in range(n):
  vote = int(input())

  if i == 0:
    dasom = vote
    continue

  heapq.heappush(heap, -vote)

res = 0
while heap:
  cur_max = -heapq.heappop(heap)
  if cur_max < dasom:
    break
  dasom += 1
  res += 1
  heapq.heappush(heap, -(cur_max-1))

print(res)