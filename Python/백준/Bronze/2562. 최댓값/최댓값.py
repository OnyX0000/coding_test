# 9개 자연수 입력받기
nums = [int(input()) for _ in range(9)]

# 최댓값과 인덱스 찾기
max_val = max(nums)
max_index = nums.index(max_val) + 1

# 결과 출력
print(max_val)
print(max_index)
