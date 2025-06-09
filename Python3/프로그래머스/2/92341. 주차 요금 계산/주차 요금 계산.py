import math
from collections import defaultdict

def convert_to_minutes(time_str) :
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def calculate_fee(total_time, fees) :
    base_time, base_fee, unit_time, unit_fee = fees
    if total_time <= base_time :
        return base_fee
    extra_time = total_time - base_time
    return base_fee + math.ceil(extra_time / unit_time) * unit_fee

def solution(fees, records) :
    in_time = dict()  # 차량별 마지막 입차 시각
    total_time = defaultdict(int)  # 차량별 총 주차 시간

    for record in records :
        time_str, car_num, status = record.split()
        minutes = convert_to_minutes(time_str)

        if status == "IN" :
            in_time[car_num] = minutes
        elif status == "OUT" :
            duration = minutes - in_time.pop(car_num)
            total_time[car_num] += duration

    # 출차되지 않은 차량은 23:59 출차 처리
    end_of_day = convert_to_minutes("23:59")
    for car_num, in_minutes in in_time.items() :
        total_time[car_num] += end_of_day - in_minutes

    # 차량 번호 기준 오름차순 정렬 및 요금 계산
    result = []
    for car_num in sorted(total_time.keys()) :
        result.append(calculate_fee(total_time[car_num], fees))

    return result
