def solution(sides):
    a, b = sorted(sides)  
    case1 = range(b + 1, a + b)
    case2 = range(b - a + 1, b + 1)
    return len(set(case1) | set(case2))
