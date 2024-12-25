def solution(t, p):
    value = int(p)
    length = len(p)
    count = 0

    for i in range(len(t) - length + 1):
        substring = t[i:i + length]
        if int(substring) <= value:
            count += 1

    return count
