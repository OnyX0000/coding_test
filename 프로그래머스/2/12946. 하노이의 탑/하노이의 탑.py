def solution(n):
    answer = []

    def move(k, a, b, c) :
        if k == 0 :
            return
        move(k - 1, a, c, b)   # 상위 n-1개: a -> b
        answer.append([a, c])     # 가장 큰 원판: a -> c
        move(k - 1, b, a, c)   # 상위 n-1개: b -> c

    move(n, 1, 2, 3)
    return answer
