def solution(survey, choices):
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    types = ['RT', 'CF', 'JM', 'AN']

    for s, c in zip(survey, choices) :
        if c < 4 :
            scores[s[0]] += 4 - c
        elif c > 4:
            scores[s[1]] += c - 4

    result = ''
    for t in types :
        result += t[0] if scores[t[0]] >= scores[t[1]] else t[1]

    return result
