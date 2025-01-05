def solution(clothes):
    # 단계 1: 해시를 사용하여 각 카테고리별 의상 수 계산
    cate_count = {}
    
    for _, category in clothes :
        cate_count[category] = cate_count.get(category, 0) + 1

    # 단계 2: 총 조합 수 계산
    # 각 카테고리에서 의상을 입지 않는 경우를 포함하여 (개수 + 1)로 계산
    total = 1
    for count in cate_count.values() :
        total *= (count + 1)

    # 단계 3: 아무것도 입지 않는 경우를 제외하기 위해 1을 뺌
    return total - 1

# 다른 풀이방법
# def solution(clothes):
#     # 단계 1: 각 카테고리별 의상 수를 수동으로 계산
#     cate_count = {}
#     for _, category in clothes :
#         if category in cate_count :
#             cate_count[category] += 1
#         else:
#             cate_count[category] = 1

#     # 단계 2: 총 조합 수 계산
#     # 각 카테고리에서 의상을 입지 않는 경우를 포함하여 (개수 + 1)로 계산
#     total = 1
#     for count in cate_count.values():
#         total *= (count + 1)

#     # 단계 3: 아무것도 입지 않는 경우를 제외하기 위해 1을 뺌
#     return total - 1