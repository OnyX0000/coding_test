def solution(n, arr1, arr2):
    answer = []

    for i in range(n) :
        # arr1과 arr2의 각 요소에 대해 OR 연산 후 이진수 문자열로 변환
        binary = bin(arr1[i] | arr2[i])[2:]
        # 이진수 문자열의 길이를 n에 맞추어 앞쪽에 0을 채움
        binary = binary.zfill(n)
        # 1을 '#'로, 0을 ' '로 변환하여 리스트에 추가
        answer.append(binary.replace('1', '#').replace('0', ' '))

    return answer