def solution(rows, columns, queries):
    # 1) 행렬 초기화
    matrix = [
        [i * columns + (j + 1) for j in range(columns)]
        for i in range(rows)
    ]
    answer = []

    # 2) 각 쿼리 처리
    for x1, y1, x2, y2 in queries :
        # 2.1) 0-index 변환
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        # 2.2) 테두리 값 수집
        values = []
        # 상단
        for y in range(y1, y2 + 1) :
            values.append(matrix[x1][y])
        # 우측
        for x in range(x1 + 1, x2 + 1) :
            values.append(matrix[x][y2])
        # 하단
        for y in range(y2 - 1, y1 - 1, -1) :
            values.append(matrix[x2][y])
        # 좌측
        for x in range(x2 - 1, x1, -1) :
            values.append(matrix[x][y1])

        # 2.3) 시계방향 한 칸 회전
        rotated = [values[-1]] + values[:-1]

        # 2.4) 회전된 값을 다시 대입
        idx = 0
        # 상단
        for y in range(y1, y2 + 1) :
            matrix[x1][y] = rotated[idx]; idx += 1
        # 우측
        for x in range(x1 + 1, x2 + 1) :
            matrix[x][y2] = rotated[idx]; idx += 1
        # 하단
        for y in range(y2 - 1, y1 - 1, -1) :
            matrix[x2][y] = rotated[idx]; idx += 1
        # 좌측
        for x in range(x2 - 1, x1, -1) :
            matrix[x][y1] = rotated[idx]; idx += 1

        # 2.5) 최소값 기록
        answer.append(min(values))

    return answer
