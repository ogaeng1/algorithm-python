def solution(N, stages):
    stage = {}
    user = len(stages)
    
    for i in range(1, N+1):
        if user != 0:
            fail = stages.count(i)
            stage[i] = fail / user
            user -= fail
        else:
            stage[i] = 0
    
    answer = sorted(stage, key=lambda x:stage[x], reverse=True)
    return answer
    