def solution(s):
    answer = ''
    temp = s.split(' ')
    
    for i in temp :
        for j in range(0, len(i)) :
            if j % 2 == 0 :
                answer += i.lower()[j].upper()
            else :
                answer += i[j].lower()
        answer += ' '  
        
    return answer[0:len(answer) - 1]