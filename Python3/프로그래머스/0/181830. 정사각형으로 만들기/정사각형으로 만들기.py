def solution(arr):
    n = max(len(arr), len(arr[0]))  
    for row in arr :
        row.extend([0] * (n - len(row)))
        
    while len(arr) < n :
        arr.append([0] * n)
        
    return arr
