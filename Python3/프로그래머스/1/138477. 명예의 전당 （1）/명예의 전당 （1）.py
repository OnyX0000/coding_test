def solution(k, score):
    hall_of_fame = []
    answer = []

    for s in score :
        # 현재 점수를 명예의 전당에 추가
        hall_of_fame.append(s)
        # 명예의 전당을 내림차순으로 정렬
        hall_of_fame.sort(reverse = True)
        # 명예의 전당의 크기를 k로 제한
        if len(hall_of_fame) > k :
            hall_of_fame.pop()  # k번째 이후 점수 제거
        # 현재 명예의 전당에서 최하위 점수를 결과에 추가
        answer.append(hall_of_fame[-1])
    
    return answer
