def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)     # 체육복을 빌리지 못한 사람
    set_reserve = set(reserve) - set(lost)  # 체육복을 빌린 사람
    
    for num in set_reserve :
        if num - 1 in set_lost :            # 번호가 하나 작은 사람에게 빌릴 경우
            set_lost.remove(num - 1)
            
        elif num + 1 in set_lost :          # 번호가 하나 큰 사람에게 빌릴 경우
            set_lost.remove(num + 1)
            
    return n - len(set_lost)