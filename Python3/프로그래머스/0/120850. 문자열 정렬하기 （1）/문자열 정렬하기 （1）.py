def solution(my_string):
    answer = []
    for i in my_string:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] :
            j = int(i)
            answer.append(j)
    answer.sort()
    return answer