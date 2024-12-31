def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0  # 각 카드 뭉치의 현재 위치를 나타내는 인덱스

    for word in goal :
        if idx1 < len(cards1) and cards1[idx1] == word :
            idx1 += 1  # cards1에서 단어를 사용
        elif idx2 < len(cards2) and cards2[idx2] == word :
            idx2 += 1  # cards2에서 단어를 사용
        else:
            return "No"  # 원하는 단어를 만들 수 없음

    return "Yes"  # 모든 단어를 순서대로 만들 수 있음