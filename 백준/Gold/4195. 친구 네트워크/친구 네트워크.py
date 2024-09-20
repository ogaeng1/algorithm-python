import sys
input = sys.stdin.readline

def find(x):
  if parent[x] == x:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)

  if x == y:
    return

  if x > y:
    parent[x] = y
    cnt[y] += cnt[x]
  else:
    parent[y] = x
    cnt[x] += cnt[y]

T = int(input())
for _ in range(T):
  friend = int(input())
  parent = {}
  cnt = {}

  for _ in range(friend):
    name1, name2 = input().split()
    
    if name1 not in parent:
      parent[name1] = name1
      cnt[name1] = 1
    if name2 not in parent:
      parent[name2] = name2
      cnt[name2] = 1

    union(name1, name2)
    print(cnt[find(name1)])