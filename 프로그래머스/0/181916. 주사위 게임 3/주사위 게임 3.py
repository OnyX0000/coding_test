def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    
    counts = {}
    for num in dice:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    if len(counts) == 1:
        p = dice[0]
        return 1111 * p
    elif len(counts) == 2:
        keys = list(counts.keys())
        values = list(counts.values())
        if 3 in values:
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            return (10 * p + q) ** 2
        else:
            p, q = keys
            return (p + q) * abs(p - q)
    elif len(counts) == 3:
        p = [k for k, v in counts.items() if v == 2][0]
        q, r = [k for k in counts if k != p]
        return q * r
    else:
        return dice[0]

