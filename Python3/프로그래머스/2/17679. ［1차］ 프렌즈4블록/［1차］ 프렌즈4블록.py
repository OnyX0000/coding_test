def solution(m, n, board):
    # 1. board를 2차원 리스트로 변환
    board = [list(row) for row in board]
    total_removed = 0

    while True :
        to_remove = set()

        # 2. 삭제할 2x2 블록 위치 탐색
        for i in range(m - 1) :
            for j in range(n - 1) :
                if board[i][j] == ' ' :
                    continue
                block = board[i][j]
                if (board[i][j+1] == block and
                    board[i+1][j] == block and
                    board[i+1][j+1] == block) :
                    to_remove |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}

        # 3. 지울 블록이 없으면 종료
        if not to_remove :
            break

        # 4. 블록 삭제
        for i, j in to_remove :
            board[i][j] = ' '
        total_removed += len(to_remove)

        # 5. 중력 시뮬레이션 (블록 내리기)
        for j in range(n) :
            empty = []
            for i in reversed(range(m)) :
                if board[i][j] == ' ':
                    empty.append(i)
                elif empty :
                    empty_i = empty.pop(0)
                    board[empty_i][j], board[i][j] = board[i][j], ' '
                    empty.append(i)

    return total_removed
