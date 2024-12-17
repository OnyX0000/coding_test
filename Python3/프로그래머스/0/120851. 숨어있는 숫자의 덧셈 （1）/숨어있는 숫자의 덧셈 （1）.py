def solution(my_string):
    answer = 0
    for i in my_string :
        if i in '1234567890' :
            answer += int(i)
    return answer