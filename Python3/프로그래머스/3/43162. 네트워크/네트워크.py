def solution(n, computers):
    # 각 컴퓨터가 이미 방문되었는지 체크하는 리스트
    visited = [False] * n
    count = 0  # 네트워크 개수를 세는 변수
    
    # 현재 컴퓨터에서 연결된 모든 컴퓨터를 방문 처리하는 함수
    def dfs(cur) :
        visited[cur] = True
        for j in range(n) :
            # 연결되어 있고 아직 방문하지 않은 컴퓨터가 있다면 재귀 호출
            if computers[cur][j] == 1 and not visited[j] :
                dfs(j)
    
    for i in range(n) :
        # 아직 방문하지 않은 컴퓨터가 있다면 새로운 네트워크 시작
        if not visited[i] :
            dfs(i)
            count += 1  # 네트워크 하나를 찾았으므로 개수 증가
            
    return count