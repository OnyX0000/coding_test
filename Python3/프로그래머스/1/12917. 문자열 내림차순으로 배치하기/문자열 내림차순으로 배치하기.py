def solution(s):
    answer = ''
    s = sorted(s)[::-1]
    for i in s :
        answer += i
    return answer