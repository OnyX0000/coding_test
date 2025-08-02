def solution(data, col, row_begin, row_end):
    # 1) 정렬: col(1-based) 오름차순, tie -> 첫 컬럼 내림차순
    col_idx = col - 1
    sorted_rows = sorted(data, key=lambda row: (row[col_idx], -row[0]))

    # 2) row_begin ~ row_end 구간의 S_i를 XOR로 누적
    hash_value = 0
    for i in range(row_begin, row_end + 1) :  # i는 1-based
        row = sorted_rows[i - 1]
        s_i = sum(v % i for v in row)        # S_i = sum of (v % i)
        hash_value ^= s_i                    # XOR 누적

    return hash_value
