from collections import deque

def bfs(x, y, graph, visit):
    q = deque([(x, y, 0)])
    visit[x][y][0] = 1

    while q:
        x, y, w = q.popleft()
        if x == N - 1 and y == M - 1:
            return visit[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny][w]:
                if graph[nx][ny] == '0':
                    q.append((nx, ny, w))
                    visit[nx][ny][w] = visit[x][y][w] + 1
                elif graph[nx][ny] == '1' and w == 0 and not visit[nx][ny][1]:
                    q.append((nx, ny, 1))
                    visit[nx][ny][1] = visit[x][y][w] + 1

    return -1

N, M = map(int, input().split())
graph = [input() for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = bfs(0, 0, graph, visit)
print(res)