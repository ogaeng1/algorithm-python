from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  visit = [-1] * 100001
  visit[n] = 0
  q = deque([n])

  while q:
    pos = q.popleft()
    if pos == k:
      return visit[pos]

    for i in (pos*2, pos-1, pos+1):
      if 0 <= i < 100001 and visit[i] == -1:
        if i == pos*2:
          visit[i] = visit[pos]
          q.appendleft(i)
        else:
          visit[i] = visit[pos]+1
          q.append(i)

n, k = map(int, input().split())
print(bfs())