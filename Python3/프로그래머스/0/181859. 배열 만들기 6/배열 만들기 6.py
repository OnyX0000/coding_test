def solution(arr):
    answer = []
    for i in range(0, len(arr)) : 
        if answer == [] :
            answer.append(arr[i])
        elif (answer != []) & (answer[-1] == arr[i]) :
            answer.pop(-1)
        elif (answer != []) & (answer[-1] != arr[i]) :
            answer.append(arr[i])
    if answer == [] :
        return [-1]
    return answer