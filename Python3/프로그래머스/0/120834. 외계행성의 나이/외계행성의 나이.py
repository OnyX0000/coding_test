def solution(age):
    answer = ''
    alpha = 'abcdefghij'
    if age < 10 :
        return alpha[age % 10]
    elif 10 <= age < 100 :
        answer += alpha[age // 10]
        answer += alpha[age % 10]
    elif 100 <= age < 1000 :
        answer += alpha[age // 100]
        answer += alpha[age % 100 // 10]
        answer += alpha[age % 100 % 10]
    else :
        return 'baaa'
    return answer