def solution(food):
    left = []
    for i in range(1, len(food)):
        count = food[i] // 2 
        left.append(str(i) * count)  
    
    right = ''.join(left)[::-1]
    
    return ''.join(left) + '0' + right