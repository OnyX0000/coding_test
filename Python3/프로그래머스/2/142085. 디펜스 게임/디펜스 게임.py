def solution(n, k, enemy):
    import heapq
    
    inv_heap = []       # 무적권을 쓸 라운드 후보(최소 힙)
    spent = 0           # 병사 누적 소모

    for i, e in enumerate(enemy) :
        heapq.heappush(inv_heap, e)   # 일단 무적권 후보로 넣고
        if len(inv_heap) > k :
            # 가장 작은 것은 무적권을 쓰지 않고 병사로 처리
            spent += heapq.heappop(inv_heap)
        if spent > n :
            # i번째 라운드 처리 불가 → 직전 라운드까지 방어
            return i

    # 전부 막을 수 있음
    return len(enemy)
