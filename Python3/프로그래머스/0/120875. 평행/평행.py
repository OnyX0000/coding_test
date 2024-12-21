def solution(dots):
    for i in range(4):
        for j in range(i + 1, 4) :
            for k in range(4) :
                for l in range(k + 1, 4) :
                    if i != k and i != l and j != k and j != l :
                        if (dots[j][1] - dots[i][1]) * (dots[l][0] - dots[k][0]) == (dots[l][1] - dots[k][1]) * (dots[j][0] - dots[i][0]) :
                            return 1
    return 0
