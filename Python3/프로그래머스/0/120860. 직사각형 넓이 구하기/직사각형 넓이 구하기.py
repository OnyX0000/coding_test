def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    x_max, x_min = max(x), min(x)
    y_max, y_min = max(y), min(y)

    width = x_max - x_min
    height = y_max - y_min

    return width * height