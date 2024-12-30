def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command  # i, j, k 값 추출
        # array의 i번째부터 j번째까지 자르고 정렬한 후 k번째 값 선택
        sliced = sorted(array[i-1:j])  # i-1부터 j까지 슬라이싱 후 정렬
        answer.append(sliced[k-1])  # k번째 값 추가
    return answer
