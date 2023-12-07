def solution(s):
    answer = 0
    for i in s:
        if answer < 0:
            break
        if i == '(':
            answer += 1
        else:
            answer -= 1
    return True if answer == 0 else False