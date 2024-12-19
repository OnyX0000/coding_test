def solution(emergency):
    sorted_emergency = sorted(enumerate(emergency), key = lambda x: x[1], reverse = True)
    rank = [0] * len(emergency)
    for order, (idx, _) in enumerate(sorted_emergency, start = 1) :
        rank[idx] = order
    return rank