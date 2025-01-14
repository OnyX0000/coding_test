def solution(arr1, arr2):
    rows = len(arr1)         # arr1의 행 개수
    cols = len(arr2[0])      # arr2의 열 개수
    n = len(arr2)            # arr2의 행 개수 = arr1의 열 개수

    # 결과 행렬 초기화
    result = [[0] * cols for _ in range(rows)]

    # 행렬 곱셈 수행
    for i in range(rows) :             # arr1의 각 행
        for j in range(cols) :         # arr2의 각 열
            for k in range(n) :        # 행렬 곱셈 계산
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result
