def solution(nums):
    answer = 0
    n = len(nums)
    
    # 3개의 수를 고르기 위한 3중 for문
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = nums[i] + nums[j] + nums[k]
                
                # 소수 판별
                if total > 1:
                    is_prime = True
                    for divisor in range(2, int(total ** 0.5) + 1):  # 제곱근 직접 계산
                        if total % divisor == 0:
                            is_prime = False
                            break
                    if is_prime:
                        answer += 1
    
    return answer
