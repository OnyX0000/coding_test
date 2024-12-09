def solution(my_string):
    answer = []
    answer = [0] * 52
    
    for char in my_string:
        if 'A' <= char <= 'Z':  # 대문자
            answer[ord(char) - ord('A')] += 1
        elif 'a' <= char <= 'z':  # 소문자
            answer[ord(char) - ord('a') + 26] += 1
    
    return answer
