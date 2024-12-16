def solution(numbers):
    nmax = max(numbers)
    numbers.remove(nmax)
    return nmax * max(numbers)