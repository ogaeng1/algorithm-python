def solution(food):
    player1 = ''
    
    for i in range(1, len(food)):
        player1 += str(i) * int(food[i] // 2)
        
    return player1 + '0' + player1[::-1]
    