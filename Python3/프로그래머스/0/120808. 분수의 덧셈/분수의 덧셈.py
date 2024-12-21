def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2

    a, b = numerator, denominator
    while b:
        a, b = b, a % b

    return [numerator // a, denominator // a]