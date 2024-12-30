def solution(k, m, score):
    score.sort(reverse=True)
    apple = [score[i:i+m] for i in range(0, len(score), m)]
    
    res = 0
    
    for i in apple:
        if len(i) == m:
            res += i[-1] * m
            
    return res
