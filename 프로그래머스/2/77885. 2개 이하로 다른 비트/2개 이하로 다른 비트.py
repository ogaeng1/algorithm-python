def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            answer.append(numbers[i]+1)
        else:
            bi = list('0' + bin(numbers[i])[2:])
            bi_idx = ''.join(bi).rindex('0')
            bi[bi_idx] = '1'
            bi[bi_idx+1] = '0'
            
            answer.append(int(''.join(bi), 2))

    return answer