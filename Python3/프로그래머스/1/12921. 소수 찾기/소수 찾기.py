def solution(n):
    # 소수는 2부터 시작하기때문에 1은 제외
    prime_nums = set(range(2, n + 1))
    
    # 소수가 아닌 경우에 prime_nums에서 제외
    for i in range(2, int(n ** 0.5) + 1) :
        if i in prime_nums :
            prime_nums -= set(range(i * 2, n + 1, i))
            
    return len(prime_nums)