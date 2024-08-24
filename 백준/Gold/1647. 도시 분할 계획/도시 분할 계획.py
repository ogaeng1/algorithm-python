import sys, heapq
input = sys.stdin.readline

def find(x):
  if x == parent[x]:
    return x
  else:
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[y] = x

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
heap = []

for _ in range(M):
  a, b, c = map(int, input().split())
  heapq.heappush(heap, (c, a, b))

edge = N-1
res = 0
cost = 0

while edge > 0:
  c, a, b = heapq.heappop(heap)
  if find(a) != find(b):
    union(a, b)
    res += c
    edge -= 1
    cost = c

print(res - cost)