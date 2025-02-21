def solution(storage, requests):
    from collections import deque

    n = len(storage)
    m = len(storage[0])
    grid = [list(row) for row in storage]

    # 외부와 연결된 빈 공간 영역을 반환하는 함수
    def get_exterior(grid) :
        exterior = [[False] * m for _ in range(n)]
        dq = deque()
        # 창고 경계에 있는 빈 셀을 시작점으로 설정
        for i in range(n) :
            for j in range(m) :
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == '.' :
                    exterior[i][j] = True
                    dq.append((i, j))
        while dq :
            x, y = dq.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m :
                    if grid[nx][ny] == '.' and not exterior[nx][ny] :
                        exterior[nx][ny] = True
                        dq.append((nx, ny))
        return exterior

    # (i, j)에 위치한 컨테이너가 접근 가능한지 판단하는 함수
    def is_accessible(i, j, grid, exterior) :
        # 4방향 중 하나라도 창고 외부와 연결되어 있으면 접근 가능
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            nx, ny = i + dx, j + dy
            # 인접 셀이 창고 외부면 바로 접근 가능
            if not (0 <= nx < n and 0 <= ny < m) :
                return True
            # 인접 셀이 비어있고, 그 빈 공간이 외부와 연결되어 있는 경우
            if grid[nx][ny] == '.' and exterior[nx][ny] :
                return True
        return False

    # 요청 처리
    for req in requests :
        container_type = req[0]  # 요청 알파벳은 첫 글자
        if len(req) == 2 :
            # 크레인 사용: 해당 타입의 모든 컨테이너 제거
            for i in range(n) :
                for j in range(m) :
                    if grid[i][j] == container_type :
                        grid[i][j] = '.'
        else :
            # 지게차 사용: 접근 가능한 컨테이너만 제거
            exterior = get_exterior(grid)
            for i in range(n) :
                for j in range(m) :
                    if grid[i][j] == container_type and is_accessible(i, j, grid, exterior) :
                        grid[i][j] = '.'

    # 남아있는 컨테이너 수 계산 후 반환
    answer = sum(1 for i in range(n) for j in range(m) if grid[i][j] != '.')
    return answer
