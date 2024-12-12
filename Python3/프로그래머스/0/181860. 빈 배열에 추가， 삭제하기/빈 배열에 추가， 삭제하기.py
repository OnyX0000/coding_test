def solution(arr, flag):
    answer = []
    for i in range(0, len(flag)) :
        if flag[i] :
            for j in range(arr[i] * 2) : 
                answer.append(arr[i])
        else :
            for k in range(arr[i]) :
                answer.pop(-1)
    return answer