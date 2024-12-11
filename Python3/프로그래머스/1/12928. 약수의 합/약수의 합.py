def solution(n):
    answer = 0
    for i in range(n + 1) :
        if n % (i + 1) :
            pass
        elif n == 0 :
            answer = 0
        else: 
            answer += (i + 1)
    return answer