def solution(my_string):
    answer = ''    
    sort_list = sorted(my_string.lower())        

    for v in range(len(sort_list)):
        answer += sort_list[v]

    return answer