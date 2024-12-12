def solution(X, Y):
    count_X = [0] * 10
    count_Y = [0] * 10
    common_digits = []

    for digit in X:
        count_X[int(digit)] += 1

    for digit in Y:
        count_Y[int(digit)] += 1
    
    for i in range(10):
        if count_X[i] > 0 and count_Y[i] > 0:
            common_digits.extend([str(i)] * min(count_X[i], count_Y[i]))

    if not common_digits:
        return "-1"
    
    common_digits.sort(reverse=True)
    result = "".join(common_digits)
    
    if result[0] == "0":
        return "0"

    return result