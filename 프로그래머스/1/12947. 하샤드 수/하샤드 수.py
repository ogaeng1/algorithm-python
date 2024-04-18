def solution(x):
    str_x = str(x)
    answer = 0
    
    for i in str_x:
        answer += int(i)
        
    return True if x % answer == 0 else False