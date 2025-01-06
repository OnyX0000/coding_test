def solution(s):
    answer = ''
    temp = s.split(' ')
    
    for i in temp :
        i = i.capitalize()
        if answer == '' :   # 처음에는 공백을 넣지 않음
            answer += i
        else :
            answer += ' '   # 처음이 아니라면 문자를 더하기 전에 공백을 추가 
            answer += i
        
    return answer