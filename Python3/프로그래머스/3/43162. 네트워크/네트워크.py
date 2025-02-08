def solution(n, computers):
    from collections import deque  # BFS 탐색을 위한 큐 사용
    
    visited = [False] * n  # 각 컴퓨터(노드)의 방문 여부를 저장하는 리스트
    answer = 0  # 네트워크 개수를 저장할 변수
    
    for i in range(n) :  # 모든 컴퓨터(노드)를 확인
        if not visited[i] :  # 아직 방문하지 않은 노드라면, 새로운 네트워크 시작
            queue = deque([i])  # BFS 탐색을 위한 큐 초기화 (시작 노드 추가)
            
            while queue :  # 큐가 빌 때까지 반복 (연결된 모든 노드 방문)
                node = queue.popleft()  # 큐에서 노드 하나 꺼내기
                visited[node] = True  # 해당 노드를 방문 처리
                
                for j in range(n) :  # 현재 노드와 연결된 다른 노드 확인
                    if computers[node][j] == 1 and not visited[j] :  
                        # 연결된 노드이며, 아직 방문하지 않았다면
                        queue.append(j)  # 해당 노드를 큐에 추가하여 다음 탐색 대상으로 설정
                        visited[j] = True  # 방문 처리 (중복 방문 방지)
            
            answer += 1  # 하나의 네트워크 탐색이 끝났으므로 네트워크 개수 증가

    return answer
