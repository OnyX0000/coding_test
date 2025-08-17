def solution(board):
    if not board or not board[0] :
        return 0

    R, C = len(board), len(board[0])
    prev = [0] * (C + 1)  # dp[i-1][*]
    best = 0

    for i in range(1, R + 1) :
        curr = [0] * (C + 1)  # dp[i][*]
        for j in range(1, C + 1) :
            if board[i-1][j-1] == 1 :
                curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1
                if curr[j] > best :
                    best = curr[j]
            # else: curr[j] = 0 (초기값 그대로)
        prev = curr

    return best * best
