def solution(numbers):
    result = []
    for x in numbers :
        if x % 2 == 0 :
            result.append(x + 1)
        else :
            # 가장 오른쪽에 있는 0을 1로 바꾸고, 그 오른쪽 1을 0으로 바꾸는 과정
            bit = 1
            while x & bit :
                bit <<= 1
            result.append((x + bit) - (bit >> 1))
    return result
