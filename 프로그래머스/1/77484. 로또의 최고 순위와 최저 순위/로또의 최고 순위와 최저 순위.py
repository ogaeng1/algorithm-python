def solution(lottos, win_nums):
    lotto_rank = [6, 6, 5, 4, 3, 2, 1]
    match_num, unknown_num = 0, 0
    
    for i in lottos:
        if i in win_nums:
            match_num += 1
        elif i == 0:
            unknown_num += 1
    
    return lotto_rank[match_num + unknown_num] ,lotto_rank[match_num]