def solution(my_strings, parts):
    answer = ''
    for string, (start, end) in zip(my_strings, parts):
        answer += string[start:end+1]
    return answer
