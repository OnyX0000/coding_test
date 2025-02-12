def solution(n, k):
    # 1. n을 k진수로 변환
    def to_base_k(n, k):
        result = ""
        while n > 0:
            result = str(n % k) + result
            n //= k
        return result
    
    # 2. 소수 판별 함수
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # 3. k진수 변환 후 '0'을 기준으로 분리하여 소수 개수 카운트
    k_base_str = to_base_k(n, k)
    prime_count = 0
    
    for part in k_base_str.split('0'):
        if part and is_prime(int(part)):
            prime_count += 1
            
    return prime_count
