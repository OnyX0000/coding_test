def solution(s):
    answer = ''
    temp = s.split(' ')
    
    for i in temp :
        i = i.capitalize()
        if answer == '' :
            answer += i
        else :
            answer += ' '
            answer += i
        
    return answer