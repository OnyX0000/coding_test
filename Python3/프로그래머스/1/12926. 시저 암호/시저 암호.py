def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    answer = []
    
    for char in s :
        if char not in low :
            if char == ' ' :
                answer.append(' ')
            else :
                shift_index = (low.index(char.lower()) + n) % 26
                answer.append(low[shift_index].capitalize())
        elif char in low :
            shift_index = (low.index(char) + n) % 26
            answer.append(low[shift_index])
            
    answer = ''.join(answer)
    return answer