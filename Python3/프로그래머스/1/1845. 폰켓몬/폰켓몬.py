def solution(nums):
    # 선택할 수 있는 폰켓몬 종류의 수는 N/2 또는 고유한 종류 수 중 작은 값
    return min(len(set(nums)), len(nums) // 2)
