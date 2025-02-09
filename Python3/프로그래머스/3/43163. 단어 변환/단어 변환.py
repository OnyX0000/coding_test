def solution(begin, target, words):
    from collections import deque
    
    # 한 글자만 다른지 확인하는 함수
    def is_one_letter_diff(word1, word2) :
        count = sum([word1[i] != word2[i] for i in range(len(word1))])
        return count == 1
    
    if target not in words :  # 목표 단어가 words에 없음
        return 0
    
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set()  # 방문한 단어 저장
    
    while queue :
        current_word, steps = queue.popleft()
        
        if current_word == target :  # 목표 단어에 도달하면 변환 횟수 반환
            return steps
        
        for word in words :
            if word not in visited and is_one_letter_diff(current_word, word) :
                queue.append((word, steps + 1))  # 다음 단계 탐색
                visited.add(word)  # 방문 처리
                
    return 0  # 변환할 수 없는 경우
