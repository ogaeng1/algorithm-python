def solution(s):
    zero, change = 0, 0
    
    while s != "1":
        zero += s.count("0")
        s = bin(s.count("1"))[2:]
        change += 1
        
    return [change, zero]