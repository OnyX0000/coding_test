def solution(storage, requests):
    from collections import deque
    
    # 창고 크기 및 2D 리스트 변환
    n, m = len(storage), len(storage[0])
    grid = [list(row) for row in storage]

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 특정 위치가 접근 가능한지 확인
    def is_accessible(x, y) :
        if x in {0, n-1} or y in {0, m-1} :  # 테두리에 위치
            return True
        return any(0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.'
                   for dx, dy in directions if (nx := x + dx, ny := y + dy))

    # BFS를 사용하여 접근 가능한 같은 알파벳 그룹 제거
    def bfs_remove(x, y, target) :
        queue = deque([(x, y)])
        grid[x][y] = '.'
        while queue :
            cx, cy = queue.popleft()
            for dx, dy in directions :
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == target and is_accessible(nx, ny) :
                    grid[nx][ny] = '.'
                    queue.append((nx, ny))

    # 출고 요청 순차 처리
    for request in requests :
        target = request[0]

        if len(request) == 1 :  # 지게차 요청
            for i in range(n) :
                for j in range(m) :
                    if grid[i][j] == target and is_accessible(i, j) :
                        bfs_remove(i, j, target)

        else:  # 크레인 요청 (해당 컨테이너 전부 제거)
            for i in range(n) :
                for j in range(m) :
                    if grid[i][j] == target :
                        grid[i][j] = '.'

    # 남은 컨테이너 개수 반환
    return sum(cell != '.' for row in grid for cell in row) + 1
