def solution(num, k): 
    answer = 0
    k = str(k)
    
    for i in str(num):
        if i != k:
            pass
        elif i == k:
            answer = (str(num).index(i))+1
        else:
            answer = -1

    if answer != 0 :
        return answer
    elif answer == 0 :
        return -1