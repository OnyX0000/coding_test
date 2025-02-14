import heapq

def solution(scoville, K):
    """
    scoville: 음식의 스코빌 지수 리스트
    K: 원하는 최소 스코빌 지수
    """
    heapq.heapify(scoville)
    mix_count = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        mix_count += 1
    
    return mix_count if scoville[0] >= K else -1