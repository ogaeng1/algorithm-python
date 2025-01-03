import sys
input = sys.stdin.readline

def dfs(x, y, idx, total):
    global res
    if res >= total + max_val * (3-idx):
        return
    if idx == 3:
        res = max(res, total)
        return res
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if idx == 1:
                    visit[nx][ny] = 1
                    dfs(x, y, idx+1, total+graph[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, idx+1, total+graph[nx][ny])
                visit[nx][ny] = 0
                
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res, max_val = 0, max(map(max, graph))

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 0, graph[i][j])
        visit[i][j] = 0
        
print(res)