def solution(my_string):
    answer = ''
    for i in my_string :
        if i in 'abcdefghijklmnopqrstuvwxyz' :
            answer += i.upper()
        else :
            answer += i.lower()
    return answer