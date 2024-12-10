def solution(arr):
    answer = 0
    while True:
        new_arr = []
        for value in arr:
            if value >= 50 and value % 2 == 0:
                new_arr.append(value // 2)
            elif value < 50 and value % 2 == 1:
                new_arr.append(value * 2 + 1)
            else:
                new_arr.append(value)
        if new_arr == arr:  # 변환 결과가 이전 배열과 같으면 종료
            return answer
        arr = new_arr
        answer += 1
