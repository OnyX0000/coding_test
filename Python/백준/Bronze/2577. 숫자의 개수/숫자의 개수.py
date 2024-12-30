# 입력 받기
A = int(input())
B = int(input())
C = int(input())

# A × B × C 계산
result = A * B * C

# 0부터 9까지의 숫자 개수를 저장할 리스트 초기화
digit_count = [0] * 10

# 결과를 문자열로 변환하여 각 숫자의 개수 세기
for digit in str(result):
    digit_count[int(digit)] += 1

# 결과 출력
for count in digit_count:
    print(count)