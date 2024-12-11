def solution(myString, pat):
    answer = ''
    a = myString.rfind(pat)
    if len(pat) == 1 :
        for i in range(len(myString)) :
            if a + 1 > i :
                answer += myString[i]
    elif len(pat) != 1 :
        for j in range(len(myString)) : 
            if a > j : 
                answer += myString[j]
        answer += myString[a:a + len(pat)]
    return answer