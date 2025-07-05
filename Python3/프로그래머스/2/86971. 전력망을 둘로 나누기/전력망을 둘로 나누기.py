from collections import deque

def bfs(start, graph, visited) :
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue :
        node = queue.popleft()
        for neighbor in graph[node] :
            if not visited[neighbor] :
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count

def solution(n, wires):
    min_diff = n  # 최대 송전탑 개수 차이의 초기값
    for i in range(len(wires)) :
        # 그래프 초기화
        graph = {i: [] for i in range(1, n + 1)}

        # 간선 하나 끊기
        for j in range(len(wires)) :
            if i == j :
                continue  # 이번에 끊을 간선
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = [False] * (n + 1)

        # 임의의 노드에서 시작하여 송전탑 개수 구하기
        count = bfs(1, graph, visited)

        # 두 전력망의 차이 계산
        diff = abs(count - (n - count))
        min_diff = min(min_diff, diff)

    return min_diff
