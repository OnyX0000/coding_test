def solution(a, b):
    x, y = a, b
    while y :
        x, y = y, x % y
    b //= x

    while b % 2 == 0 :
        b //= 2
    while b % 5 == 0 :
        b //= 5

    return 1 if b == 1 else 2