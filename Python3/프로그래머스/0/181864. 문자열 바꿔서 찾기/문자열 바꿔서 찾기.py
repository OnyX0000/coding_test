def solution(myString, pat):
    transformed = ''.join('B' if char == 'A' else 'A' for char in myString)
    return 1 if pat in transformed else 0