def solution(n):
    temp = []
    answer = ''
    for i in str(n) :
        temp.append(i)
    
    for j in sorted(temp)[::-1] :
        answer += j
        
    return int(answer)