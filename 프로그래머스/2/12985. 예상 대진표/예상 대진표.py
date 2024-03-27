import math

def solution(n,a,b):
    answer = 0

    while a != b:
        a = math.floor(a / 2 + 0.5)
        b = math.floor(b / 2 + 0.5)
        answer += 1

    return answer