def solution(n):
    zero_cnt = bin(n)[2:].count('1')
    
    while True:
        n += 1
        if bin(n)[2:].count('1') == zero_cnt:
            return n