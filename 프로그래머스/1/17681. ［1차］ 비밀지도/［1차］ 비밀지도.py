def solution(n, arr1, arr2):
    answer = []
    for marker1, marker2 in zip(arr1, arr2):
        bi = str(bin(marker1 | marker2))[2:]
        bi = '0' * (n - len(bi)) + bi
        bi = bi.replace('0', ' ')
        bi = bi.replace('1', '#')
        answer.append(bi)
    return answer