def solution(wallpaper):
    lux, luy = 50, 50
    rdx, rdy = 0, 0

    for i, row in enumerate(wallpaper) :
        for j, cell in enumerate(row) :
            if cell == '#' :
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)

    return [lux, luy, rdx, rdy]