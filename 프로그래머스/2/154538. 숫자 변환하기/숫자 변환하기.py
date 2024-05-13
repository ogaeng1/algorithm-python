from collections import deque

def solution(x, y, n):
    visit = [False] * 1000001
    q = deque([(x, 0)])
    
    while q:
        cur, cnt = q.popleft()
        
        if cur == y:
            return cnt
        
        operation = [cur + n, cur * 2, cur * 3]
        for i in operation:
            if 0 <= i <= 1000000 and not visit[i]:
                visit[i] = True
                q.append((i, cnt + 1))
        
    return -1
    