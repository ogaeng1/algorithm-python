import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y, visit, island, w, h):
    visit[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and not visit[nx][ny] and island[nx][ny] == 1:
            dfs(nx, ny, visit, island, w, h)

def islandCount(w, h, island):
    visit = [[False] * w for _ in range(h)]
    res = 0

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and not visit[i][j]:
                dfs(i, j, visit, island, w, h)
                res += 1

    return res

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = [list(map(int, input().split())) for _ in range(h)]
    print(islandCount(w, h, island))