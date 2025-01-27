def solution(n, times):
    left, right = 1, max(times) * n  # 시간의 범위 설정
    answer = right
    
    while left <= right :
        mid = (left + right) // 2  # 중간 시간 계산
        people = sum(mid // time for time in times)  # mid 시간 내 처리 가능한 사람 수 계산
        
        if people >= n :  # 처리 가능한 사람이 n명 이상이면
            answer = mid  # 가능한 시간을 저장
            right = mid - 1  # 더 짧은 시간 시도
        else :
            left = mid + 1  # 더 긴 시간 필요
            
    return answer
