def solution(intStrs, k, s, l):
    temp = []

    for i in intStrs:
        temp2 = i[s:s+l]
        if int(temp2) > k :
            temp += [int(temp2)]
        else :
            continue
            
    answer = temp
    return answer