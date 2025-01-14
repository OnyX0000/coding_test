def solution(n, left, right):
    lr, lc = left // n, left % n
    rr, rc = right // n, right % n
    a = []

    for i in range(lr, rr+1) :
        j = i + 1
        a += ([j] * j + list(range(j + 1, n + 1)))

    return a[lc:(rr - lr) * n + rc + 1]    