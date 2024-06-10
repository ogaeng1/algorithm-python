import sys
from collections import deque
input = sys.stdin.readline

def bfs():  
  while water or dochi:
    for _ in range(len(water)):
      x, y = water.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
          graph[nx][ny] = '*'
          water.append((nx, ny))

    for _ in range(len(dochi)):
      x, y, t = dochi.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
          if graph[nx][ny] == 'D':
            return t + 1
          if graph[nx][ny] == '.':
            graph[nx][ny] = 'S'
            dochi.append((nx, ny, t+1))

  return 'KAKTUS'

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

water = deque()
dochi = deque()
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
  for j in range(c):
    if graph[i][j] == '*':
      water.append((i, j))
    elif graph[i][j] == 'S':
      dochi.append((i, j, 0))

print(bfs())