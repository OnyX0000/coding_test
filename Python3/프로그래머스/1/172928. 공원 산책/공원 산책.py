def solution(park, routes):
    H, W = len(park), len(park[0])
    x, y = next((i, j) for i, row in enumerate(park) for j, cell in enumerate(row) if cell == 'S')
    moves = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    for route in routes :
        direction, steps = route.split()
        dx, dy = moves[direction]
        steps = int(steps)
        nx, ny = x, y
        valid = True

        for _ in range(steps) :
            nx, ny = nx + dx, ny + dy
            if not (0 <= nx < H and 0 <= ny < W) or park[nx][ny] == 'X' :
                valid = False
                break

        if valid :
            x, y = nx, ny

    return [x, y]
