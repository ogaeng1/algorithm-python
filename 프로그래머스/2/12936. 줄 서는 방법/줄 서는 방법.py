import math

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    
    while arr:
        res = (k-1) // math.factorial(n-1)
        answer.append(arr.pop(res))
        
        k = k % math.factorial(n-1)
        n -= 1
        
    return answer