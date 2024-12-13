def solution(num_list):
    answer = []
    i = 0
    
    while i < 5 :
        answer.append(min(num_list))
        num_list.remove(min(num_list))
        i += 1
    
    num_list.sort()
    return num_list