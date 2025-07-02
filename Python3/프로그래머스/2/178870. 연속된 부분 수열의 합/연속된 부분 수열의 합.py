def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    min_length = float('inf')
    answer = [0, 0]
    current_sum = sequence[0]

    while right < n :
        if current_sum < k :
            right += 1
            if right < n :
                current_sum += sequence[right]
        elif current_sum > k :
            current_sum -= sequence[left]
            left += 1
        else :
            # 현재 부분 수열의 길이
            current_length = right - left + 1
            if current_length < min_length :
                min_length = current_length
                answer = [left, right]
            
            # 다음 경우를 찾기 위해 left를 이동
            current_sum -= sequence[left]
            left += 1

    return answer
