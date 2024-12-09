def solution(arr):
    answer = []
    if 2 not in arr: 
        return [-1]
    
    start = arr.index(2)
    end = len(arr) - 1 - arr[::-1].index(2)
    
    answer = arr[start:end+1]

    return answer