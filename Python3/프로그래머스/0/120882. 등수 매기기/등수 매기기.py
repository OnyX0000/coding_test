def solution(score):
    averages = [(s[0] + s[1]) / 2 for s in score]

    ranked = sorted(averages, reverse = True)
    ranks = [ranked.index(avg) + 1 for avg in averages]

    return ranks