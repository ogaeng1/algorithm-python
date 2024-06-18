import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, size):
    visit = [[False] * n for _ in range(n)]
    visit[x][y] = True
    eat = []
    q = deque([(x, y, 0)])

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if graph[nx][ny] <= size:
                    visit[nx][ny] = True
                    q.append((nx, ny, dist + 1))
                    if 0 < graph[nx][ny] < size:
                        eat.append((dist + 1, nx, ny))

    eat.sort()
    return eat

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0
            break

size = 2
eat_fish = res = 0

while True:
    eat = bfs(x, y, size)
    if not eat:
        break

    dist, fx, fy = eat[0]
    res += dist
    eat_fish += 1
    x, y = fx, fy
    graph[fx][fy] = 0

    if eat_fish == size:
        size += 1
        eat_fish = 0

print(res)
