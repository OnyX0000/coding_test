def solution(s):
    answer = 0
    now_count = 0
    diff_count = 0
    now = s[0]
    
    for i in range(len(s)) :
        if now == s[i] :
            now_count += 1
        else :
            diff_count += 1
        
        if now_count == diff_count :
            answer += 1
            now_count = 0
            diff_count = 0
            if i < (len(s) - 1) : 
                now = s[i + 1]
    
    if now_count != 0 :
        answer += 1
    
    return answer