def solution(people, limit):
    boat = 0
    people.sort()
    
    minWeight, maxWeight = 0, len(people) - 1
    
    while minWeight <= maxWeight:
        if people[minWeight] + people[maxWeight] <= limit:
            minWeight += 1
        maxWeight -= 1
        boat += 1
    
    return boat