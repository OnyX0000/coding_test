def solution(keymap, targets):
    # 문자별 최소 키 입력 횟수 저장 딕셔너리
    min_key_presses = {}

    # keymap을 순회하며 문자별 최소 입력 횟수를 저장
    for i, keys in enumerate(keymap) :
        for j, char in enumerate(keys) :
            if char not in min_key_presses :
                min_key_presses[char] = j + 1  # 인덱스는 0부터 시작하므로 +1
            else :
                min_key_presses[char] = min(min_key_presses[char], j + 1)

    # 결과 저장 리스트
    result = []

    # targets를 순회하며 최소 입력 횟수 계산
    for target in targets :
        key_presses = 0
        possible = True
        for char in target :
            if char in min_key_presses :
                key_presses += min_key_presses[char]
            else :
                # 작성할 수 없는 문자 발견 시 -1 저장 후 종료
                possible = False
                break
        if possible :
            result.append(key_presses)
        else :
            result.append(-1)
    
    return result
