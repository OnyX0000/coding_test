def solution(n, k):
    import math
    
    nums = list(range(1, n + 1))  # 후보 숫자들
    answer = []

    k -= 1  # 인덱스는 0-based 이므로 보정

    for i in range(n, 0, -1) :
        fact = math.factorial(i - 1)
        index = k // fact
        answer.append(nums.pop(index))
        k %= fact

    return answer
