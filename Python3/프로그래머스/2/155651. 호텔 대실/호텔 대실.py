import heapq

def time_to_minutes(time_str) :
    """시간 문자열을 분 단위로 변환하는 함수"""
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes
 
def solution(book_time) :
    # 시간 단위로 변환 및 정렬
    book_time = sorted([[time_to_minutes(start), time_to_minutes(end) + 10] for start, end in book_time])
    
    room_heap = []  # 각 객실의 종료 시간 관리용 min heap
    
    for start, end in book_time :
        if room_heap and room_heap[0] <= start :
            # 기존 객실 재사용
            heapq.heappop(room_heap)
        
        # 새로운 예약을 heap에 추가
        heapq.heappush(room_heap, end)
    
    return len(room_heap)
