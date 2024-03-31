def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for i in clothes:
        clothes_type = i[1]
        
        if clothes_type in clothes_dict:
            clothes_dict[clothes_type] += 1
        else:
            clothes_dict[clothes_type] = 1

    for i in clothes_dict.values():
        answer *= i + 1
        
    return answer-1