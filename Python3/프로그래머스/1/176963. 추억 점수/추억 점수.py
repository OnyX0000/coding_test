def solution(name, yearning, photo):
    # 이름과 그리움 점수를 딕셔너리로 매핑
    yearning_dict = {n: y for n, y in zip(name, yearning)}
    
    # 각 사진의 추억 점수를 계산
    result = []
    for people in photo:
        # 각 사진의 인물에 대해 추억 점수를 합산
        score = sum(yearning_dict.get(person, 0) for person in people)
        result.append(score)
    
    return result