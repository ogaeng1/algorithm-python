import sys
input = sys.stdin.readline

def bfs(x, y, d):
    cnt = 0
    while True:
        if room[x][y] == 0:
            room[x][y] = 2
            cnt += 1
            
        for i in range(4):
            d = (d-1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
                x, y = nx, ny
                break
            
        else:
            nx = x - dx[d]
            ny = y - dy[d]
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] != 1:
                x, y = nx, ny
            else:
                return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(bfs(r, c, d))