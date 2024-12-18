def solution(n):
    arr = [[0] * n for a in range(n)]
    
    for i in range(n) :
        arr[i][i] = 1
    
    return arr
