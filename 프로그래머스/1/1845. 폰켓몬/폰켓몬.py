def solution(nums):
    monster = len(set(nums))
    select = len(nums) // 2
    
    return min(monster, select)
    