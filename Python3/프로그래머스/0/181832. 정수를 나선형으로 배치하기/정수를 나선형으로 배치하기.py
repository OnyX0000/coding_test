def solution(n):
    matrix = [[0] * n for _ in range(n)]
    x, y, num, dx, dy = 0, 0, 1, 0, 1

    while num <= n * n:
        matrix[x][y] = num
        num += 1
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            dx, dy = dy, -dx  # 방향 전환
        x, y = x + dx, y + dy

    return matrix