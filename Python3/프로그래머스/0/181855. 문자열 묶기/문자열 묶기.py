def solution(strArr):
    answer = 0
    length_counts = {}

    for s in strArr :
        length = len(s)
        if length in length_counts :
            length_counts[length] += 1
        else:
            length_counts[length] = 1

    answer = max(length_counts.values())
    return answer
