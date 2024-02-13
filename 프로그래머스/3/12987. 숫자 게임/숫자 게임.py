from collections import deque

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    A, B = deque(A), deque(B)
    
    while B:
        if B[0] > A[0]:
            A.popleft()
            B.popleft()
            answer += 1
        else:
            B.popleft()
            
    return answer