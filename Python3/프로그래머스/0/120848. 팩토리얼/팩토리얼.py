def solution(n):
    answer = 0
    ftr = 1
    i = 1
    while ftr <= n :
        ftr *= i
        i += 1
    return i - 2