from collections import deque

n, k = map(int, input().split())
test_tube = []
virus = []

for i in range(n):
  test_tube.append(list(map(int, input().split())))
  for j in range(n):
    if test_tube[i][j] != 0:
      virus.append((test_tube[i][j], 0, i, j))

virus.sort()
q = deque(virus)

s, x, y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while q:
  v, s1, x1, y1 = q.popleft()
  if s1 == s:
    break

  for i in range(4):
    nx = x1 + dx[i]
    ny = y1 + dy[i]
    
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if test_tube[nx][ny] == 0:
        test_tube[nx][ny] = v
        q.append((v, s1+1, nx, ny))

print(test_tube[x-1][y-1])