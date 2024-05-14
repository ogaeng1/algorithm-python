# 2차원 리스트를 활용

def solution(n):
    answer = []
    triangle = [[0] * i for i in range(1, n+1)]   # 길이에 맞는 2차원 리스트 생성
    x, y = 0, 0   # 항상 꼭짓점이 1로 시작하니까 시작 좌표는 0, 0
    dir = [(1, 0), (0, 1), (-1, -1)]   # 방향. 반시계 방향으로 순회하니까 아래, 오른쪽, 위 3가지 방향만 있으면 됨
    end = sum(i for i in range(1, n+1))   # 삼각형의 마지막 번호
    turn, pos = 0, 1  #  방향 회전과 위치
    
    # dfs 나 bfs 처럼 4방향이 아닌 3방향으로 생각하고 순회.
    # 범위를 벗어나지 않고, 방문하려고 하는 곳이 0이라면(아직 방문하지 않았다면) 숫자 채우고
    # 그게 아니라면 방향 전환
    while pos <= end:
        triangle[x][y] = pos
        pos += 1
        
        dx, dy = dir[turn]
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < n and triangle[nx][ny] == 0:
            x, y = nx, ny
        else:
            turn = (turn+1) % 3
            dx, dy = dir[turn]
            x += dx
            y += dy
    
    for row in triangle:
        for num in row:
            answer.append(num)
            
    return answer