def solution(tickets):
    visited = {}    # 방문할 공항 딕셔너리 생성 

    # 공항 정렬 후 딕셔너리에 삽입
    for start, end in sorted(tickets) :
        if start in visited :
            visited[start].append(end)
        else:
            visited[start] = [end]

    route = []  # 최종 경로 저장 리스트

    def dfs(airport) :
        while airport in visited and visited[airport] :  # 현재 공항에서 출발할 수 있는 공항이 남아있다면
            next_airport = visited[airport].pop(0)  # 알파벳 순서대로 방문
            dfs(next_airport)  # 재귀 호출
        route.append(airport)  # 더 이상 갈 곳이 없으면 경로에 추가

    dfs("ICN")  # "ICN"에서 시작
    
    return route[::-1]  # 경로를 뒤집어서 반환
