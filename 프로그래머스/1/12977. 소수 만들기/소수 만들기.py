import math
from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        total = sum(i)
        check = True
        
        for j in range(2, int(math.sqrt(total) + 1)):
            if total % j == 0:
                check = False
                break
        if check is True:
            answer += 1

    return answer