def solution(operations):
    import heapq
    
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙
    valid = {}  # 동기화 관리 딕셔너리

    for op in operations :
        command, value = op.split()
        value = int(value)

        if command == "I" :  # 삽입 연산
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)  # 최대 힙을 위해 음수로 저장
            valid[value] = valid.get(value, 0) + 1  # 삽입된 개수 추적

        elif command == "D" :
            if not valid :
                continue  # 큐가 비어 있으면 삭제 무시

            if value == 1 :  # 최댓값 삭제
                while max_heap and valid[-max_heap[0]] == 0 :
                    heapq.heappop(max_heap)  # 동기화되지 않은 값 제거
                
                if max_heap :
                    max_val = -heapq.heappop(max_heap)
                    valid[max_val] -= 1

            elif value == -1 :  # 최솟값 삭제
                while min_heap and valid[min_heap[0]] == 0 :
                    heapq.heappop(min_heap)  # 동기화되지 않은 값 제거
                
                if min_heap :
                    min_val = heapq.heappop(min_heap)
                    valid[min_val] -= 1

    # 최종적으로 동기화된 힙을 확인하여 남아있는 값 결정
    while max_heap and valid[-max_heap[0]] == 0 :
        heapq.heappop(max_heap)
    
    while min_heap and valid[min_heap[0]] == 0 :
        heapq.heappop(min_heap)

    if not min_heap or not max_heap :
        return [0, 0]

    return [-max_heap[0], min_heap[0]]