def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))

    # 정렬 기준 정의: lambda를 사용하여 효율적으로 처리
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 정렬 후 모든 문자열을 이어 붙임
    result = ''.join(numbers)

    # 결과가 '0'으로 시작하는 경우 (모든 원소가 0인 경우)
    return result if result[0] != '0' else '0'