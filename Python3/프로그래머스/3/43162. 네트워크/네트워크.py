def solution(n, computers):
    visited = [False] * n    # 방문 여부 기록
    count = 0                # 네트워크 개수 

    for i in range(n) :
        if not visited[i] :  # 아직 방문할 곳이 남았다면 BFS 시작
            queue = [i]
            visited[i] = True

            while queue :    
                current = queue.pop(0)
                # 현재 있는 곳부터 모든 곳을 탐색
                for j in range(n) :
                    if computers[current][j] == 1 and not visited[j] :
                        visited[j] = True
                        queue.append(j)
            count += 1

    return count