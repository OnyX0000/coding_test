def solution(s):
    answer = []
    record = {}
    
    for idx, c in enumerate(s) :
        if c in record:
            answer.append(idx - record[c])
        else :
            answer.append(-1)
        record[c] = idx
            
    return answer