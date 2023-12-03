def solution(d, budget):
    answer, price = 0, 0
    d.sort()
    
    for i in d:
        price += i
        if price <= budget:
            answer += 1
    return answer