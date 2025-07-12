def solution(N, road, K):
    import heapq
    
    # 인접 리스트 초기화
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road :
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 최소 거리 테이블
    distance = [float('inf')] * (N + 1)
    distance[1] = 0  # 1번 마을에서 자기 자신까지의 거리
    
    # 우선순위 큐: (거리, 마을 번호)
    queue = [(0, 1)]
    
    while queue :
        dist, now = heapq.heappop(queue)
        
        if dist > distance[now] :
            continue  # 이미 처리된 노드
        
        for neighbor, cost in graph[now] :
            new_cost = dist + cost
            if new_cost < distance[neighbor] :
                distance[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
    
    # K 이하 거리인 마을 개수 세기
    return sum(1 for d in distance if d <= K)
