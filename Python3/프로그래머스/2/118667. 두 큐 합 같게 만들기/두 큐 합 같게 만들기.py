def solution(queue1, queue2):
    q = queue1 + queue2
    n = len(queue1)
    
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 != 0 :
        return -1  # 절대 같게 만들 수 없음

    target = total_sum // 2

    left = 0
    right = n
    curr_sum = sum(queue1)

    max_ops = n * 3  # 최악의 경우를 커버할 연산 한도
    ops = 0

    while ops <= max_ops :
        if curr_sum == target :
            return ops
        elif curr_sum > target :
            curr_sum -= q[left]
            left += 1
        else :
            curr_sum += q[right % (2 * n)]
            right += 1
        ops += 1

    return -1
