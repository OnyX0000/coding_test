def solution(n):
    # 1. 삼각형 구조 초기화
    triangle = [ [0] * (i+1) for i in range(n) ]
    
    # 2. 이동 방향: 아래 → 오른쪽 → 왼쪽 위
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    
    x, y = 0, 0  # 시작 위치
    num = 1      # 채울 숫자
    direction = 0  # 방향 인덱스 (0: 아래, 1: 오른쪽, 2: 왼쪽 위)
    
    for i in range(n * (n + 1) // 2) :
        triangle[y][x] = num
        num += 1
        
        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 범위 초과 or 이미 채워짐 → 방향 전환
        if ny >= n or nx > ny or triangle[ny][nx] != 0 :
            direction = (direction + 1) % 3
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        x, y = nx, ny
    
    # 결과를 1차원 배열로 변환
    answer = []
    for row in triangle :
        answer.extend(row)
    
    return answer
