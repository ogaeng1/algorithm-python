from itertools import permutations

def prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def solution(numbers):
    answer = 0
    num_list = [i for i in numbers]
    per_res = []
    
    for i in range(1, len(num_list)+1):
        for j in permutations(num_list, i):
            per_res.append(int(''.join(j)))
            
    per_res = set(per_res)
    
    for i in per_res:
        if prime(i):
            answer += 1
            
    return answer