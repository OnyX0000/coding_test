def solution(n):
    answer = 1
    temp = []
    
    if n > 2 :
        for i in range(1, (n // 2) + 2) :
            temp.append(i)
            if sum(temp) > n :
                while sum(temp) > n :
                    temp.pop(0)
            if sum(temp) == n :
                answer += 1
        return answer
    else :
        return 1

# 효율성 테스트 0
# def solution(n):
#     answer = 0
    
#     for i in range(1, n + 1) :
#         temp = 0
#         for j in range(i, n + 1) :
#             temp += j
#             if temp == n :
#                 answer += 1
                
#     return answer