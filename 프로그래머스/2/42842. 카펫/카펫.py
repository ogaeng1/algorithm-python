def solution(brown, yellow):
    vertical = 1
    horizontal = (brown - vertical * 2) // 2
    
    while True:
        if (vertical * (horizontal-2)) == yellow:
            break
        vertical += 1
        horizontal = (brown - vertical * 2) // 2
        
    return [horizontal, vertical+2]