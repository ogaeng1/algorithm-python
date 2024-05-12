def dfs(com, visit, n):
    visit[n] = True
    
    for i in range(len(com)):
        if com[n][i] == 1 and not visit[i]:
            dfs(com, visit, i)
            
def solution(n, computers):
    answer = 0
    visit = [False] * n
    
    for i in range(n):
        if not visit[i]:
            dfs(computers, visit, i)
            answer += 1
            
    return answer