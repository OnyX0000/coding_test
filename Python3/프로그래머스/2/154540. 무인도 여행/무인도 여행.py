def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start_x, start_y):
        queue = [(start_x, start_y)]  
        visited[start_x][start_y] = True
        total_food = int(maps[start_x][start_y])

        while queue:
            x, y = queue.pop(0)  
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    total_food += int(maps[nx][ny])
                    queue.append((nx, ny))

        return total_food

    results = []

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != 'X' and not visited[i][j]:
                max_days = bfs(i, j)
                results.append(max_days)

    return sorted(results) if results else [-1]