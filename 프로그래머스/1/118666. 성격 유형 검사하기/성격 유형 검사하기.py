from collections import defaultdict

def solution(survey, choices):
    score = defaultdict(int)
    mbti1, mbti2 = ['R' , 'C' , 'J', 'A'], ['T', 'F', 'M', 'N']
    answer = ''
    
    for (i, j), choice in zip(survey, choices):
        if choice < 4:
            score[i] += 4 - choice
        else:
            score[j] += choice - 4
    
    for m1, m2 in zip(mbti1, mbti2):
        if score[m1] > score[m2] or (score[m1] == score[m2] and m1 < m2):
            answer += m1
        else:
            answer += m2
            
    return answer