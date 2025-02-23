def convertTime(n) :
    # 입력된 정수 n을 시간과 분으로 해석하여 분 단위로 변환
    # 예: 1013 → 10시 13분 → 10*60 + 13 = 613분
    h = n // 100
    m = n % 100
    return h * 60 + m

def solution(schedules, timelogs, startday) :
    answer = 0
    
    # 각 직원의 출근 기록을 확인
    for i in range(len(schedules)) :
        s = startday  # 현재 요일 (1:월요일, 2:화요일, ..., 7:일요일)
        schedule = convertTime(schedules[i])  # 직원 i의 희망 출근 시간 (분 단위)
        
        # 일주일(7일) 동안의 출근 기록을 순서대로 검사
        for time in timelogs[i] :
            # 토요일(6)과 일요일(7)은 이벤트에 영향을 주지 않으므로 건너뛴다.
            if s in [6, 7] :
                s += 1  # 다음 요일로 이동
                if s == 8 :  # 요일이 8이면 일요일을 넘어서 월요일(1)로 변경
                    s = 1
                continue

            t = convertTime(time)  # 실제 출근 시간을 분 단위로 변환

            # 만약 실제 출근 시간이 지각이면
            # 해당 직원은 상품 대상에서 제외되므로 반복문을 종료한다.
            if schedule + 10 < t :
                break
            else : 
                s += 1  # 다음 근무일로 이동
        else :
            # for-else: 반복문이 break 없이 정상 종료되면,
            # 모든 유효 근무일(월~금)에 제시간 출근한 것으로 간주하여 당첨
            answer += 1

    return answer