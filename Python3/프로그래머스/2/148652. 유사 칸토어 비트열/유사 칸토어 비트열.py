def solution(n, l, r):
    def cantor_bit_count(n, start, end):
        if n == 0:
            return 1 if start <= 0 <= end else 0

        length = 5 ** n
        third = length // 5
        total = 0

        segments = [
            (0, third - 1),
            (third, 2 * third - 1),
            (2 * third, 3 * third - 1),
            (3 * third, 4 * third - 1),
            (4 * third, 5 * third - 1)
        ]

        for i, (seg_start, seg_end) in enumerate(segments):
            if start > seg_end or end < seg_start:
                continue  
            if i == 2:  
                continue
            total += cantor_bit_count(n - 1, max(0, start - seg_start), min(third - 1, end - seg_start))

        return total

    return cantor_bit_count(n, l - 1, r - 1)
