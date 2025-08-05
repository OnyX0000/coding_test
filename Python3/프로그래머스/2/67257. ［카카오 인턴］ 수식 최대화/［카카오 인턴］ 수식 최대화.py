def solution(expression):
    from itertools import permutations
    
    # 1) 토큰화
    nums, ops = [], []
    cur = ""
    for ch in expression :
        if ch.isdigit() :
            cur += ch
        else :
            nums.append(int(cur))
            ops.append(ch)
            cur = ""
    nums.append(int(cur))  # 마지막 숫자

    # 등장한 연산자 집합
    uniq_ops = tuple(sorted(set(ops)))
    # 연산자 조합(순열)
    orders = permutations(uniq_ops)

    def apply(a, b, op) :
        if op == '+' :
            return a + b
        if op == '-' :
            return a - b
        # op == '*'
        return a * b

    def evaluate(order) :
        # 원본을 보존하기 위해 복사
        n = nums[:]
        o = ops[:]
        # 우선순위 높은 연산자부터 단계적으로 처리
        for oper in order :
            new_nums = [n[0]]
            new_ops = []
            for i, op in enumerate(o) :
                if op == oper :
                    # 직전 피연산자(new_nums[-1])와 다음 피연산자(n[i+1])를 연산하여 축약
                    new_nums[-1] = apply(new_nums[-1], n[i+1], op)
                else :
                    new_nums.append(n[i+1])
                    new_ops.append(op)
            n, o = new_nums, new_ops
        # 최종 하나 남은 값
        return abs(n[0])

    # 모든 우선순위 조합 중 최대 절댓값
    answer = 0
    for order in orders :
        answer = max(answer, evaluate(order))
    return answer
