# 입력 받기
room_number = input()

# 숫자 카운팅 배열
count = [0] * 10

# 각 숫자의 빈도수 계산
for digit in room_number:
    count[int(digit)] += 1

# 6과 9는 서로 대체 가능
six_nine_count = count[6] + count[9]
count[6] = (six_nine_count + 1) // 2  # 올림 처리
count[9] = 0  # 이미 6으로 합쳤으므로 9는 고려하지 않음

# 필요한 세트의 최소 개수
result = max(count)
print(result)
