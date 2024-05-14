# 투 포인터 알고리즘

def solution(sequence, k):
    leng = len(sequence)
    answer = [0, leng]
    start, end = 0, 0
    cur_sum = sequence[0]
    
    while end < leng:
        if cur_sum < k:
            end += 1
            if end < leng:
                cur_sum += sequence[end]
        elif cur_sum > k:
            cur_sum -= sequence[start]
            start += 1
            
            if cur_sum == k and end - start < answer[1] - answer[0]:
                answer = [start, end]
            
        else:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            end += 1
            
            if end < leng:
                cur_sum += sequence[end]
            
    return answer