def solution(name, yearning, photo):
    answer = []
    
    friends = dict(zip(name, yearning))
    
    for i in photo:
        score = 0
        
        for j in i:
            score += friends.get(j, 0)
        answer.append(score)
        
    return answer