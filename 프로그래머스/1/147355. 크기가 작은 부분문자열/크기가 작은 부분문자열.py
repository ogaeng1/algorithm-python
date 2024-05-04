def solution(t, p):
    answer = 0
    t_len, p_len = len(t), len(p)
    
    for i in range((t_len - p_len) + 1):
        if int(p) >= int(t[i:i + p_len]):
            answer += 1

    return answer