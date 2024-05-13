# n 을 k진법으로 변환
# 0을 기준으로 나누고, 각 수가 소수인지 판별

def convert_num(n, k):
    res = ''
    
    while n > 0:
        res += str(n % k)
        n //= k
    res = res[::-1]
    
    return res


def prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(n, k):
    answer = 0
    change_num = convert_num(n, k).split("0")
    
    for i in change_num:
        if i:
            i = int(i)
            if prime(i):
                answer += 1
                
    return answer
