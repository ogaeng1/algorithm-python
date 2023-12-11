from collections import deque

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)

    if (sum1 + sum2) % 2:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    l = len(queue1)
    
    while cnt < 4*l:
        if sum1 == sum2:
            return cnt
        elif sum1 > sum2:
            el = queue1.popleft()
            sum1 -= el
            queue2.append(el)
            sum2 += el
        else:
            el =queue2.popleft()
            sum2 -= el
            queue1.append(el)
            sum1 += el
        cnt += 1
    return -1