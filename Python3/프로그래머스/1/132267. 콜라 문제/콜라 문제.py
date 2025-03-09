def solution(a, b, n):
    return (n - b) // (a - b) * b

# def solution(a, b, n):
#     answer = 0

#     while n >= a :
#         # 교환 가능한 콜라의 병 수
#         exchanged = (n // a) * b
#         # 남은 빈 병 수
#         remaining = n % a
#         # 총 병 수 갱신
#         n = exchanged + remaining
#         # 받은 콜라 누적
#         answer += exchanged

#     return answer