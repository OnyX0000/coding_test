def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 이동을 위한 방향 벡터
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 방문 여부를 기록할 2차원 배열 초기화
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 리스트를 큐처럼 사용합니다.
    # 각 원소는 (현재 x, 현재 y, 현재까지 이동한 칸의 개수)를 의미합니다.
    queue = [(0, 0, 1)]
    index = 0  # 큐의 현재 인덱스
    
    while index < len(queue) :
        x, y, steps = queue[index]
        index += 1
        
        # 목표 지점에 도달했다면 이동 횟수를 반환합니다.
        if x == n - 1 and y == m - 1 :
            return steps
        
        # 4방향 탐색
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵의 범위 내에 있고, 아직 방문하지 않았으며, 벽이 없는 경우
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and maps[nx][ny] == 1 :
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))
    
    # 목표 지점에 도달할 수 없을 때 -1 반환
    return -1