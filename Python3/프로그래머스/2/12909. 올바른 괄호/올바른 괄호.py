def solution(s):
    a = 0
    
    # '('가 먼저 나와야하고 그 이후에 ')'와 개수가 다르면 False
    for i in s :
        if i == '(' :
            a += 1
        else:
            a -= 1
            
        if a < 0 :
            break
            
    return a == 0   # '('와 ')'의 개수가 같으면 True, 아니면 False