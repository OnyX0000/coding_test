def solution(board):
    from collections import deque
    
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    
    # 상하좌우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # R, G 위치 찾기
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 'R' :
                start = (i, j)
            if board[i][j] == 'G' :
                goal = (i, j)
    
    queue = deque()
    queue.append((*start, 0))
    visited[start[0]][start[1]] = True
    
    while queue :
        x, y, cnt = queue.popleft()
        
        # 목표 도착
        if (x, y) == goal :
            return cnt
        
        for dx, dy in directions :
            nx, ny = x, y
            
            # 장애물이나 벽에 닿을 때까지 직진
            while True :
                tx, ty = nx + dx, ny + dy
                if 0 <= tx < n and 0 <= ty < m and board[tx][ty] != 'D' :
                    nx, ny = tx, ty
                else :
                    break
            
            # 도착한 위치가 미방문이면 큐에 추가
            if not visited[nx][ny] :
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
    
    return -1
