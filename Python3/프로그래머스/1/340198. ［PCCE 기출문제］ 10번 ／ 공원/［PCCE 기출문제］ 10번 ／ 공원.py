def solution(mats, park):
    mats.sort(reverse=True)  # 큰 돗자리부터 확인

    for mat_size in mats :
        for x in range(len(park) - mat_size + 1) :
            for y in range(len(park[0]) - mat_size + 1) :
                # mat_size 크기의 돗자리가 해당 위치에 깔 수 있는지 확인
                if all(park[i][j] == '-1' for i in range(x, x + mat_size) for j in range(y, y + mat_size)) :
                    return mat_size

    return -1  # 깔 수 있는 돗자리가 없으면 -1 반환