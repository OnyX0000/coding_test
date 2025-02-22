def solution(n):
    factors = []
    divisor = 2

    while n > 1 :
        while n % divisor == 0 : 
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n : 
            if n > 1 :
                factors.append(n)
                break

    return sorted(set(factors))