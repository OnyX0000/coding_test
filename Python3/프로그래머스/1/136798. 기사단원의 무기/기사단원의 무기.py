def solution(number, limit, power):
    answer = 0

    for knight in range(1, number + 1) :
        # 약수 개수를 직접 계산
        count = 0
        for i in range(1, int(knight ** 0.5) + 1) :
            if knight % i == 0 :
                count += 1
                if i != knight // i :
                    count += 1
        # 제한 수치 초과 시 power로 대체
        attack_power = count if count <= limit else power
        answer += attack_power

    return answer
