from collections import Counter

def solution(topping):
    answer = 0
    bro1 = Counter(topping)
    bro2 = {}
            
    for i in topping:
        if len(bro1) == len(bro2):
            answer += 1
            
        if i not in bro2:
            bro2[i] = 1
            
        bro1[i] -= 1
        
        if bro1[i] == 0:
            del bro1[i]
            
    return answer