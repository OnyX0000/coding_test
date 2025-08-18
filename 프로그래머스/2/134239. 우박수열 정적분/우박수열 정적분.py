def solution(k, ranges):
    # 1) 우박수열 y값 생성 (끝 1 포함)
    y = [k]
    while y[-1] != 1 :
        cur = y[-1]
        if cur % 2 == 0 :
            y.append(cur // 2)
        else :
            y.append(cur * 3 + 1)

    # 2) 인접 구간 사다리꼴 면적 전처리: areas[i] = 구간 (i -> i+1) 면적
    #    prefix[i] = 0..i-1 구간 총합 (길이 L 이면 구간은 L-1개)
    L = len(y)
    areas = [ (y[i] + y[i + 1]) / 2.0 for i in range(L - 1) ]
    prefix = [0.0]
    for a in areas :
        prefix.append(prefix[-1] + a)  # prefix[j] = 0..j-1 합

    # 3) 각 쿼리 처리
    answer = []
    last_idx = L - 1                # 마지막 점 인덱스
    last_seg_idx = L - 1            # 마지막 구간의 끝 인덱스 기준으로 end 계산
    for a, b in ranges :
        start = a
        end = last_seg_idx + b      # end는 구간의 '끝 인덱스' 의미 (구간은 0..L-2)

        # 유효성 검사
        if start < 0 or end < 0 or start > last_seg_idx or end > last_seg_idx :
            answer.append(-1.0)
            continue
        if start > end :
            answer.append(-1.0)
            continue
        if start == end :
            answer.append(0.0)
            continue

        # 구간 [start, end) 의 면적 합 = prefix[end] - prefix[start]
        # (end는 포함되지 않는 오른쪽 경계)
        area = prefix[end] - prefix[start]
        answer.append(area)

    return answer
