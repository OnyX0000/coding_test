from collections import deque

def solution(maps) :
    n, m = len(maps), len(maps[0])

    # 위치 찾기
    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 'S' :
                start = (i, j)
            elif maps[i][j] == 'L' :
                lever = (i, j)
            elif maps[i][j] == 'E' :
                exit_ = (i, j)

    # BFS 함수 정의
    def bfs(start_pos, target_char) :
        visited = [[False]*m for _ in range(n)]
        queue = deque()
        queue.append((start_pos[0], start_pos[1], 0))  # (x, y, 거리)
        visited[start_pos[0]][start_pos[1]] = True

        while queue :
            x, y, dist = queue.popleft()
            if maps[x][y] == target_char :
                return dist

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)] :
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                    if maps[nx][ny] != 'X' :
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
        return -1

    dist_S_to_L = bfs(start, 'L')
    if dist_S_to_L == -1 :
        return -1

    dist_L_to_E = bfs(lever, 'E')
    if dist_L_to_E == -1 :
        return -1

    return dist_S_to_L + dist_L_to_E
