def solution(board):
    n = len(board)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    danger = set()

    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                danger.add((i, j))
                for dx, dy in directions :
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n :
                        danger.add((nx, ny))

    return n * n - len(danger)