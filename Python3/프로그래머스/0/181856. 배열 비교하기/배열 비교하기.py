def solution(arr1, arr2):
    answer = 0
    tempa = 0
    tempb = 0
    if len(arr1) > len(arr2) :
        return 1
    elif len(arr1) < len(arr2) :
        return -1
    elif len(arr1) == len(arr2) :
        for i in arr1 :
            tempa += i
        for j in arr2 :
            tempb += j
        if tempa > tempb :
            return 1
        elif tempa < tempb :
            return -1
        else :
            return 0
    return answer