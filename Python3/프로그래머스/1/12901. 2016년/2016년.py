def solution(a, b):
    # 2016년 각 월의 일수를 리스트로 정의 (윤년이므로 2월은 29일)
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1월 1일이 금요일이므로 요일 배열을 정의
    weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    # 1월 1일부터 a월 b일까지의 총 일수 계산
    total_days = sum(days_in_month[:a-1]) + b
    
    # 1월 1일이 금요일이므로, 금요일은 5번째 인덱스 (0부터 시작)
    # 1월 1일 기준으로 (total_days - 1)일 뒤의 요일을 구함
    day_of_week = (total_days - 3) % 7
    
    return weekdays[day_of_week]

