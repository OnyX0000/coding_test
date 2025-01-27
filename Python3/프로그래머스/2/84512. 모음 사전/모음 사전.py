def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    mult = [781, 156, 31, 6, 1] 
    
    for i, char in enumerate(word) :
        answer += vowels.index(char) * mult[i] + 1
    
    return answer
