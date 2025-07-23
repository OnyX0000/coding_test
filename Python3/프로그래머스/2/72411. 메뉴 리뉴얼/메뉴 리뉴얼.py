def solution(orders, course):
    from itertools import combinations
    from collections import Counter
    
    result = []

    for c in course :
        combs = []
        for order in orders :
            sorted_order = sorted(order)
            combs += combinations(sorted_order, c)
        
        # 조합 빈도수 계산
        comb_counter = Counter(combs)

        if not comb_counter :
            continue
        
        # 최소 2회 이상 등장한 조합만 대상
        max_count = max(comb_counter.values())
        if max_count < 2 :
            continue

        # 최대 빈도수 조합만 선택
        for menu, count in comb_counter.items() :
            if count == max_count :
                result.append("".join(menu))
    
    # 사전 순 정렬
    return sorted(result)
