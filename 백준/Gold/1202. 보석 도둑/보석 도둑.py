import heapq, sys
input = sys.stdin.readline

max_heap = []
jewel, bag = [], []

N, K = map(int, input().split())
for _ in range(N):
  bosuk = list(map(int, input().split()))
  jewel.append(bosuk)

for _ in range(K):
  bag.append(int(input()))

jewel.sort(key=lambda x: x[0])
bag.sort()
j = 0
price = 0

for i in bag:
  while j < N and i >= jewel[j][0]:
    heapq.heappush(max_heap, -jewel[j][1])
    j += 1

  if max_heap:
    price -= heapq.heappop(max_heap)

print(price)