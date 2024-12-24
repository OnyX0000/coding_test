def solution(arr):
    temp = min(arr)
    arr.remove(temp)
    return [-1] if arr == [] else arr