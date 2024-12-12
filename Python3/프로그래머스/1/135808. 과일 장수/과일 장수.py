def solution(k, m, score):
    score.sort(reverse=True)
    max_profit = 0
    
    for i in range(0, len(score), m):
        box = score[i:i + m]
        if len(box) == m:
            max_profit += min(box) * m

    return max_profit
