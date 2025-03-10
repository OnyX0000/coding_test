def solution(land):
    n = len(land)

    for i in range(1, n) :  # 첫 번째 행은 그대로 사용
        for j in range(4) :  # 4개의 열을 각각 갱신
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)

    return max(land[n-1])  # 마지막 행에서 최대값 반환
