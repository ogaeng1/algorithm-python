from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visit = [[False] * m for _ in range(n)]
    visit[0][0] = True
    q = deque()
    q.append((0, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    
    
