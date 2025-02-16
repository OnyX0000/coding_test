def solution(triangle):
    n = len(triangle)  # 삼각형의 높이
    
    # 아래에서부터 위로 올라가면서 테이블 갱신
    for i in range(n - 2, -1, -1) :  # 아래에서 두 번째 줄부터 시작
        for j in range(i + 1) :  # 각 층의 원소 순회
            # 현재 위치의 값 + 아래층에서 선택 가능한 두 값 중 큰 값
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    return triangle[0][0]  # 꼭대기에 저장된 최대 경로 합 반환
