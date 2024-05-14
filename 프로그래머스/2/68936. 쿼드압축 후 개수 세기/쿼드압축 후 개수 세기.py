def solution(arr):
    def dc(x, y, n):
        pos = arr[x][y]
        
        for i in range(x, x+n):
            for j in range(y, y+n):
                if pos != arr[i][j]:
                    m = n // 2
                    
                    return dc(x, y, m) + dc(x, y+m, m) + dc(x+m, y, m) + dc(x+m, y+m, m)

        return [pos]
    
    answer = dc(0, 0, len(arr))
    return [answer.count(0), answer.count(1)]