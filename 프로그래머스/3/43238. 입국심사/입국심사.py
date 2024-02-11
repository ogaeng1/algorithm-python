def solution(n, times):
    answer = 0
    start, end = min(times), max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        
        for i in range(len(times)):
            cnt += mid // times[i]
            
        if cnt >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
            
    return answer