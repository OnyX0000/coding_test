def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],  # 1번 수포자
        [2, 1, 2, 3, 2, 4, 2, 5],  # 2번 수포자
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자
    ]
    
    scores = [0] * 3  # 3명의 수포자 점수 초기화
    
    for i, answer in enumerate(answers) :
        for j, pattern in enumerate(patterns) :
            if answer == pattern[i % len(pattern)] :
                scores[j] += 1
    
    max_score = max(scores)
    
    # 가장 많이 맞춘 사람들의 번호를 구함
    return [i + 1 for i, score in enumerate(scores) if score == max_score]
