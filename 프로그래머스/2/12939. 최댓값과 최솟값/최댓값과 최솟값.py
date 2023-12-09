def solution(s):
    s = s.split()
    s = [int(i) for i in s]
    
    return f"{min(s)} {max(s)}"
    