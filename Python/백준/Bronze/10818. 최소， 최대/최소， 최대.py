# 정수 입력받기 
n = int(input())
nums = list(map(int, input().split()))

# 최솟값과 최댓값 찾기
min_val = min(nums)
max_val = max(nums)

# 결과 출력
print(min_val, max_val)
