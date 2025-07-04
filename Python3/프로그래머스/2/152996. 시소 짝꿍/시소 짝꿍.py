def solution(weights):
    from collections import Counter
    from fractions import Fraction

    count = Counter(weights)
    weights = sorted(count.keys())
    result = 0

    # 각 몸무게마다 경우의 수 체크
    for i, w in enumerate(weights) :
        # 같은 몸무게끼리는 조합 공식으로 계산
        if count[w] >= 2 :
            result += count[w] * (count[w] - 1) // 2

        # 비율에 맞는 상대 몸무게를 탐색
        for ratio in [Fraction(2, 3), Fraction(1, 2), Fraction(3, 4)] :
            target = w * ratio.denominator // ratio.numerator
            if (w * ratio.denominator) % ratio.numerator != 0 :
                continue  # 정수가 아닐 경우 제외
            if target in count :
                result += count[w] * count[target]

    return result
