def solution(n):
    temp = []
    for i in range(1, n + 1) :
        if n % i == 1 :
            temp.append(i)
    return min(temp)