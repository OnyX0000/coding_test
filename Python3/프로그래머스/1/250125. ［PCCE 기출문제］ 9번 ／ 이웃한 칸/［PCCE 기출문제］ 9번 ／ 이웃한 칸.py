def solution(board, h, w):
    # 보드의 크기
    n = len(board)
    # 카운트를 저장할 변수
    count = 0
    # h와 w의 변화량을 나타내는 리스트
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    # 현재 칸의 색깔
    current_color = board[h][w]
    
    # 인접한 4개의 방향을 확인
    for i in range(4) :
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        # 보드 범위를 벗어나지 않는지 확인
        if 0 <= h_check < n and 0 <= w_check < n :
            # 같은 색깔인지 확인
            if board[h_check][w_check] == current_color :
                count += 1
    
    return count
