def solution(s, skip, index):
    alpha = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip] * 5
    return ''.join([alpha[alpha.index(i) + index] for i in s])
            