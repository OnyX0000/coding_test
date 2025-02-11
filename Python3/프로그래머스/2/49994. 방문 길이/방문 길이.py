def solution(dirs):
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    
    x, y = 0, 0  # 시작 위치
    visited_paths = set()  # 지나간 길 저장
    
    for direction in dirs:
        dx, dy = moves[direction]
        nx, ny = x + dx, y + dy  # 이동할 위치 계산
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:  # 좌표 범위 내에서만 이동
            # 지나간 길을 (현재 위치 → 이동 후 위치)와 (이동 후 위치 → 현재 위치)로 저장
            visited_paths.add((x, y, nx, ny))
            visited_paths.add((nx, ny, x, y))
            
            # 좌표 업데이트
            x, y = nx, ny
    
    return len(visited_paths) // 2  # 왕복을 제거하여 길 개수 계산
