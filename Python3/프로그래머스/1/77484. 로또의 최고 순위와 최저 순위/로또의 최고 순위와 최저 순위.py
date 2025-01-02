def solution(lottos, win_nums):
    answer = []
    cnt = 0
    z_cnt = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    for lotto in lottos :
        if lotto in win_nums :
            cnt += 1
        elif lotto == 0 :
            z_cnt += 1
    
    return [rank[cnt + z_cnt], rank[cnt]]