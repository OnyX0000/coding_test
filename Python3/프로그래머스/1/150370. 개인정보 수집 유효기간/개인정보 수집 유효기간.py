def solution(today, terms, privacies):
    today_days = int(today[:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
    term_dict = {t.split()[0]: int(t.split()[1]) * 28 for t in terms}
    result = []
    
    for i, privacy in enumerate(privacies) :
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        expire_date = year * 12 * 28 + month * 28 + day + term_dict[term]
        if expire_date <= today_days :
            result.append(i + 1)

    return result
