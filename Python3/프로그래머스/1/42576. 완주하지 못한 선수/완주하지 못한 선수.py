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

# 다른 풀이
# def solution(participant, completion):
#     # 해시 값을 이용한 합산
#     hash_sum = 0
#     hash_dict = {}
    
#     # 참가자 해시값을 더하고 해시 테이블에 기록
#     for person in participant :
#         hash_val = hash(person)
#         hash_sum += hash_val
#         hash_dict[hash_val] = person

#     # 완주한 사람의 해시값을 빼기
#     for person in completion :
#         hash_sum -= hash(person)

#     # 남은 해시값으로 완주하지 못한 사람 찾기
#     return hash_dict[hash_sum]