def solution(myString, pat):
    answer = 0
    temp = []
    for i in range(0, len(myString)) :
        temp.append(myString[i:i+len(pat)])
    for j in temp :
        if j == pat :
            answer += 1
        else :
            answer += 0
    
    return answer