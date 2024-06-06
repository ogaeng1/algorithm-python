import sys, heapq
input = sys.stdin.readline

min_heap, max_heap = [], []
problem = {}
N = int(input())

for _ in range(N):
  P, L = map(int, input().split())
  problem[P] = L
  heapq.heappush(min_heap, (L, P))
  heapq.heappush(max_heap, (-L, -P))
  
M = int(input())
for _ in range(M):
  command = input().split()
  if command[0] == 'recommend':
    if command[1] == '1':
      while True:
        L, P = -max_heap[0][0], -max_heap[0][1]
        if problem[P] == L:
          print(P)
          break
        heapq.heappop(max_heap)
    else:
      while True:
        L, P = min_heap[0]
        if problem[P] == L:
          print(P)
          break
        heapq.heappop(min_heap)
  elif command[0] == 'add':
    P, L = int(command[1]), int(command[2])
    problem[P] = L
    heapq.heappush(min_heap, (L, P))
    heapq.heappush(max_heap, (-L, -P))
  else:
    P = int(command[1])
    problem[P] = -1