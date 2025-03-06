def solution(msg):
    # 1. 길이가 1인 모든 단어를 포함하는 사전 초기화 (A~Z)
    dictionary = {chr(i + 65): i + 1 for i in range(26)}
    next_index = 27  # 새로운 색인 번호
    
    result = []  # 출력 결과 리스트
    i = 0
    
    while i < len(msg):
        w = msg[i]  # 현재 입력
        
        while i + 1 < len(msg) and w + msg[i + 1] in dictionary:
            w += msg[i + 1]
            i += 1
        
        # 현재 입력(w)의 색인 번호를 출력 리스트에 추가
        result.append(dictionary[w])
        
        # 처리되지 않은 다음 글자가 남아있다면 새로운 단어(w+c) 사전에 추가
        if i + 1 < len(msg):
            dictionary[w + msg[i + 1]] = next_index
            next_index += 1
        
        i += 1  # 다음 문자로 이동
    
    return result