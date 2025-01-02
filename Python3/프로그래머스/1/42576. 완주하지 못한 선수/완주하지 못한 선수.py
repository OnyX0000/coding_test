def solution(participant, completion):
    # 정렬을 통해 두 리스트를 비교
    participant.sort()
    completion.sort()
    
    # 완주하지 못한 선수를 찾기
    for p, c in zip(participant, completion) :
        if p != c :
            return p
    
    # 마지막 남은 선수가 완주하지 못한 선수
    return participant[-1]
