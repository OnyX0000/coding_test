def solution(arr):
    from collections import Counter

    def compress(x, y, size) :
        # 첫 값 기준으로 동일한지 검사
        initial = arr[x][y]
        for i in range(x, x + size) :
            for j in range(y, y + size) :
                if arr[i][j] != initial :
                    break
            else :
                continue
            break
        else:
            return Counter({initial : 1})

        # 4개로 분할하여 재귀적으로 탐색
        half = size // 2
        counts = Counter()
        counts += compress(x, y, half)  # 좌상
        counts += compress(x, y + half, half)  # 우상
        counts += compress(x + half, y, half)  # 좌하
        counts += compress(x + half, y + half, half)  # 우하
        return counts

    counts = compress(0, 0, len(arr))
    return [counts[0], counts[1]]
