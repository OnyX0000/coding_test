def solution(polynomial):
    terms = polynomial.split(' + ')
    x_term = 0
    constant = 0

    for term in terms :
        if 'x' in term :
            if term == 'x' :
                x_term += 1
            else:
                x_term += int(term[:-1])
        else:
            constant += int(term)

    result = []
    
    if x_term :
        result.append(f'{x_term}x' if x_term != 1 else 'x')
    if constant :
        result.append(str(constant))

    return ' + '.join(result)