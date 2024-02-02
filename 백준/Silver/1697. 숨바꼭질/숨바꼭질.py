from collections import deque

def bfs(start, goal):
  visited = [False] * 100001
  q = deque([(start, 0)])

  while q:
    cur_position, time = q.popleft()

    if cur_position == goal:
      return time

    distance = [cur_position-1, cur_position+1, cur_position*2]
    for i in distance:
      if 0 <= i <= 100000 and not visited[i]:
        visited[i] = True
        q.append((i, time + 1))

n, k = map(int, input().split())
print(bfs(n, k))