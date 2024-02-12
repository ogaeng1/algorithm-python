from itertools import product

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = []
    
    for i in range(1, 6):
        for j in product(alpha, repeat=i):
            answer.append(''.join(j))
            
    answer.sort()
    
    return answer.index(word) + 1