def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees :
        filtered = "".join([s for s in tree if s in skill])  # 필요한 스킬 추출
        if skill.startswith(filtered) :  # skill의 앞부분과 일치해야 유효
            answer += 1

    return answer
