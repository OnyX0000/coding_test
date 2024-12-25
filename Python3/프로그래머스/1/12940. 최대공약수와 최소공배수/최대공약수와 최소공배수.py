def solution(n, m):
    a, b = n, m
    while b :
        a, b = b, a % b
    gcd_value = a
    lcm_value = n * m // gcd_value
    return [gcd_value, lcm_value]
