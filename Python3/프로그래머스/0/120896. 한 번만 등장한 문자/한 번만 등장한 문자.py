def solution(s):
    answer = ''
    for i in s :
        if s.count(i) == 1 :
            answer += i
    temp = sorted(answer) 
    answer = ''
    for i in temp :
        answer += i
    return answer
            