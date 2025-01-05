def solution(bandage, health, attacks):
    answer = health  # 현재 체력
    clear = 0  # 연속으로 붕대를 감은 시간
    attack_time = []  # 몬스터 공격 시간 리스트

    # 몬스터 공격 시간 추출
    for i in range(len(attacks)) :
        attack_time.append(attacks[i][0])

    # 시뮬레이션 진행
    for i in range(attack_time[-1] + 1) :  # 마지막 공격 시간까지 반복
        if i in attack_time:  # 공격 시간이면
            pos = attack_time.index(i)  # 해당 공격 인덱스
            power = attacks[pos][1]  # 공격 데미지
            answer -= power  # 체력 감소
            clear = 0  # 붕대 초기화
            if answer <= 0 :  # 체력이 0 이하라면 사망
                answer = -1
                break
        else:  # 공격 시간이 아닐 때
            if answer < health :  # 체력이 최대 체력보다 낮으면
                answer += bandage[1]  # 회복량 적용
                clear += 1  # 붕대 시간 증가
                if clear == bandage[0] :  # 붕대 완료 시 추가 회복
                    answer += bandage[2]
                    clear = 0  # 붕대 초기화
            if answer > health :  # 최대 체력 초과 방지
                answer = health

    return answer
