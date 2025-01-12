def solution(n, a, b):
    round_num = 0
    a -= 1
    b -= 1

    while a != b :
        a //= 2
        b //= 2
        round_num += 1

    return round_num