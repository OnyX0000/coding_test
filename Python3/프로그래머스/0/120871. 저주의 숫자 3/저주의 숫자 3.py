def solution(n):
    count = 0
    a = 0

    while count < n :
        a += 1
        if a % 3 != 0 and '3' not in str(a) :
            count += 1

    return a