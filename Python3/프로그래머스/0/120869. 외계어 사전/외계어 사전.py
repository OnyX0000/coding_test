def solution(spell, dic):
    spell_sorted = ''.join(sorted(spell))

    for word in dic :
        if ''.join(sorted(word)) == spell_sorted :
            return 1
    return 2
