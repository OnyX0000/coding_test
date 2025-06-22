from itertools import permutations

def is_prime(n: int) -> bool :
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def solution(numbers: str) -> int :
    # 모든 길이에 대한 순열을 한 번에 집계
    nums = {
        int(''.join(p))
        for r in range(1, len(numbers) + 1)
        for p in permutations(numbers, r)
    }
    return sum(is_prime(n) for n in nums)
