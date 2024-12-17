def solution(a, b):
    if (a + b) % 2 == 1 :
        return 2 * (a + b)
    else :
        if a % 2 == 0 :
            return abs(a - b)
        else :
            return a * a + b * b