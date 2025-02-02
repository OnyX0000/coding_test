def make_multiset(s) :
    s = s.lower()  # 대소문자 구분 없이 처리
    multiset = []
    
    for i in range(len(s) - 1) :
        pair = s[i:i + 2]
        if pair.isalpha() :  # 두 글자가 모두 알파벳인지 확인
            multiset.append(pair)
    
    return multiset

def get_intersection_union(multiset1, multiset2) :
    intersection, union = 0, 0
    used = set(multiset1 + multiset2)  # 중복 포함한 모든 원소 집합
    
    for item in used :
        count1 = multiset1.count(item)
        count2 = multiset2.count(item)
        intersection += min(count1, count2)  # 교집합은 최소 개수
        union += max(count1, count2)  # 합집합은 최대 개수
    
    return intersection, union

def solution(str1, str2) :
    # 다중집합 생성
    multiset1 = make_multiset(str1)
    multiset2 = make_multiset(str2)
    
    # 교집합 및 합집합 계산
    intersection, union = get_intersection_union(multiset1, multiset2)

    # 자카드 유사도 계산
    jaccard = 1 if union == 0 else intersection / union

    # 결과 변환 후 반환
    return int(jaccard * 65536)

# def solution(str1, str2) :
#     list1 = [str1[n:n + 2].lower() for n in range(len(str1) - 1) if str1[n:n + 2].isalpha()]
#     list2 = [str2[n:n + 2].lower() for n in range(len(str2) - 1) if str2[n:n + 2].isalpha()]

#     tlist = set(list1) | set(list2)
#     res1 = [] #합집합
#     res2 = [] #교집합

#     if tlist :
#         for i in tlist :
#             res1.extend([i]*max(list1.count(i), list2.count(i)))
#             res2.extend([i]*min(list1.count(i), list2.count(i)))

#         answer = int(len(res2) / len(res1) * 65536)
#         return answer

#     else :
#         return 65536