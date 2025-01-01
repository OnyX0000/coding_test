def solution(n, m, section):
    answer = 0  # 페인트를 칠한 횟수
    current_position = 0  # 롤러가 현재 덮고 있는 끝 위치
    
    for s in section :
        # 롤러가 이미 덮고 있는 범위에 현재 구역이 포함되지 않으면 롤러를 다시 시작
        if s > current_position :
            # 롤러를 칠하고, 덮은 범위의 끝을 current_position에 기록
            answer += 1
            current_position = s + m - 1  # 롤러가 덮을 수 있는 마지막 구역
    
    return answer
